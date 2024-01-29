from django.db import models
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _
from .choices import CurrencyTypeChoices
from .constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=6, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=6, decimal_places=2)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    currency_type = models.SmallIntegerField(
        _('Currency type'), choices=CurrencyTypeChoices.choices, default=CurrencyTypeChoices.EUR)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

    def __str__(self):
        return f'Buy: {self.buy}, Sell: {self.sell}, Source: {self.source}'


class ContactUs(models.Model):
    email_from = models.EmailField(_('Email form'))
    subject = models.CharField(_('Subject'), max_length=80)
    message = models.CharField(_('Message'), max_length=255)
    name = models.CharField(_('Name'), max_length=64, default='Unknown')
    body = models.CharField(_('Body'), max_length=2048, blank=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'Subject: {self.subject}, Mail: {self.email_from}'


def source_directory_path(instance, filename):
    return f'logos/source_{instance.id}/{filename}'


class Source(models.Model):
    source_url = models.CharField(_('Source URL'), max_length=255)
    name = models.CharField(_('Name'), max_length=64)
    code_name = models.CharField(_('Code Name'), max_length=64, unique=True)
    logo = models.FileField(_('Logo'), default=None, blank=True, null=True, upload_to=source_directory_path)

    class Meta:
        verbose_name = 'Source'
        verbose_name_plural = 'Sources'

    def __str__(self):
        return f'Source: {self.name}'

    @property
    def logo_url(self) -> str:
        if self.logo:
            return self.logo.url
        if self.name == 'PrivatBank' or self.code_name == PRIVATBANK_CODE_NAME:
            return static('privatlogo.png')
        elif self.name == 'MonoBank' or self.code_name == MONOBANK_CODE_NAME:
            return static('monologo.jpeg')


class RequestResponseLog(models.Model):
    path = models.CharField(_('Path'), max_length=64)
    request_method = models.CharField(_('Request Method'), max_length=10)
    time = models.DecimalField(_('Time'), max_digits=5, decimal_places=3)

    class Meta:
        verbose_name = 'RequestResponseLog'
        verbose_name_plural = 'RequestResponseLogs'

    def __str__(self):
        return f'Path: {self.path}, Request method: {self.request_method}, Time: {self.time}, sec'
