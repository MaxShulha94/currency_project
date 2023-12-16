from django.db import models

from .choices import CurrencyTypeChoices


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    currency_type = models.SmallIntegerField(choices=CurrencyTypeChoices.choices, default=CurrencyTypeChoices.UAH)
    source = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

    def __str__(self):
        return f'Buy: {self.buy}, Sell: {self.sell}, Source: {self.source}'


class ContactUs(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'Subject: {self.subject}, Mail: {self.email_from}'


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Source'
        verbose_name_plural = 'Sources'

    def __str__(self):
        return f'Source: {self.name}'
