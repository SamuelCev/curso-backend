# Generated by Django 5.0.1 on 2024-03-10 00:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecommerce", "0004_productmodel_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="state",
            field=models.CharField(
                choices=[
                    ("PU", "PUBLICADO"),
                    ("BR", "BORRADOR"),
                    ("PR", "PRIVADO"),
                ],
                default="BR",
                max_length=2,
            ),
        ),
    ]
