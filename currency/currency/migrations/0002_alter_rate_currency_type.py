# Generated by Django 4.2.7 on 2024-01-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='currency_type',
            field=models.SmallIntegerField(choices=[(1, 'Dollar'), (2, 'Euro')], default=2, verbose_name='Currency type'),
        ),
    ]
