# Generated by Django 2.2.16 on 2020-10-12 08:30
import os
from django.db import migrations


def forwards_func(apps, schema_editor):
    os.system('python manage.py loaddata shopuser');


def reverse_func(apps, schema_editor):
 apps.get_model("mainapp", "ShopUser").objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)
    ]
