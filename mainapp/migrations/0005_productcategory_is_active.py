# Generated by Django 2.2.24 on 2021-11-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_fill_db"),
    ]

    operations = [
        migrations.AddField(
            model_name="productcategory",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="категория активна"),
        ),
    ]
