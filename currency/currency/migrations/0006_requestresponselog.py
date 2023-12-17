# Generated by Django 4.2.7 on 2023-12-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0005_alter_contactus_options_alter_rate_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=64, verbose_name='Path')),
                ('request_method', models.CharField(max_length=10, verbose_name='Request Method')),
                ('time', models.SmallIntegerField(verbose_name='Time')),
            ],
        ),
    ]
