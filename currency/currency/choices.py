from django.db import models


class CurrencyTypeChoices(models.IntegerChoices):
    USD = 1, 'Dollar'
    EUR = 2, 'Euro'
    UAH = 3, 'Hryvnia'
