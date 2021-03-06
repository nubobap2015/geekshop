# Generated by Django 2.2.16 on 2020-11-04 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='ключ подтверждения'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 13, 56, 37, 760497, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
