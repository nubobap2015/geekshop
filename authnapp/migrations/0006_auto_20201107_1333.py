# Generated by Django 2.2.16 on 2020-11-07 13:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0005_create_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 9, 13, 33, 7, 69829, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]