# Generated by Django 2.2.16 on 2020-10-13 18:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mainapp", "0004_fill_db"),
    ]

    operations = [
        migrations.CreateModel(
            name="Basket",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantity", models.PositiveIntegerField(default=0, verbose_name="количество")),
                ("add_datetime", models.DateTimeField(auto_now_add=True, verbose_name="время добавления")),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mainapp.Product")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="basket", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
