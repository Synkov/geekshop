# Generated by Django 2.2.24 on 2021-12-08 21:26

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
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 21, 26, 56, 645479, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
