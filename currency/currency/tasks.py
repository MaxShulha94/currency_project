import requests
from celery import shared_task
from currency.choices import CurrencyTypeChoices
from currency.constants import PRIVATBANK_CODE_NAME, PRIVATBANK_SOURCE_URL, MONOBANK_CODE_NAME, MONOBANK_SOURCE_URL
from currency.models import Rate, Source
from currency.utils import to_2_places_decimal
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def parse_privatbank():
    source_url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    response = requests.get(source_url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=PRIVATBANK_CODE_NAME,
                                             defaults={'name': 'PrivatBank', 'source_url': PRIVATBANK_SOURCE_URL})

    rates = response.json()

    available_currency_types = {
        'USD': CurrencyTypeChoices.USD, 'EUR': CurrencyTypeChoices.EUR
    }

    for rate in rates:
        buy = to_2_places_decimal(rate['buy'])
        sell = to_2_places_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        currency_type = available_currency_types[currency_type]
        last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('created').first()
        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                buy=buy,
                sell=sell,
                currency_type=currency_type,
                source=source
            )


@shared_task
def parse_monobank():
    source_url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(source_url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=MONOBANK_CODE_NAME,
                                             defaults={'name': 'MonoBank', 'source_url': MONOBANK_SOURCE_URL})

    rates = response.json()

    available_currency_types = {
        840: CurrencyTypeChoices.USD, 978: CurrencyTypeChoices.EUR
    }
    for rate in rates:
        if rate['currencyCodeA'] == 840 and rate['currencyCodeB'] == 980:
            currency_type = available_currency_types[840]
            buy = to_2_places_decimal(rate['rateBuy'])
            sell = to_2_places_decimal(rate['rateSell'])
        elif rate['currencyCodeA'] == 978 and rate['currencyCodeB'] == 980:
            currency_type = available_currency_types[978]
            buy = to_2_places_decimal(rate['rateBuy'])
            sell = to_2_places_decimal(rate['rateSell'])
        else:
            continue

        # currency_type = available_currency_types[currency_type]
        last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('created').first()
        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                buy=buy,
                sell=sell,
                currency_type=currency_type,
                source=source
            )


@shared_task(autoretry_for=(ConnectionError,), retry_kwargs={'max_retries': 5})
def send_email_in_background(subject, body):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
