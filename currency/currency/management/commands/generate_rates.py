import random

from django.core.management.base import BaseCommand
from currency.models import Rate, Source
from currency.choices import CurrencyTypeChoices


class Command(BaseCommand):
    help_info = "Generates 100 random rates"

    def handle(self, *args, **options):
        source, _ = Source.objects.get_or_create(
            code_name='dummy',
            defaults={
                'name': 'Dummy Source'
            }
        )
        for _ in range(100):
            Rate.objects.create(
                buy=random.randint(15, 80),
                sell=random.randint(15, 80),
                currency_type=random.choice(CurrencyTypeChoices.choices)[0],
                source=source,
            )
