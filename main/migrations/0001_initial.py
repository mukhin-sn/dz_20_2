# Generated by Django 5.0.1 on 2024-02-01 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="наименование")),
                (
                    "description",
                    models.CharField(max_length=200, verbose_name="описание"),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="наименование")),
                (
                    "description",
                    models.CharField(max_length=200, verbose_name="описание"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="products/",
                        verbose_name="изображение",
                    ),
                ),
                ("price_for_one", models.IntegerField(verbose_name="цена за штуку")),
                (
                    "date_of_creation",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "last_modified_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата последнего изменения"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        max_length=50,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.category",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]
