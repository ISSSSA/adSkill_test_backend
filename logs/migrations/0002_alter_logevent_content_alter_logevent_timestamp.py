# Generated by Django 5.1.2 on 2024-10-11 18:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logevent',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='logevent',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
