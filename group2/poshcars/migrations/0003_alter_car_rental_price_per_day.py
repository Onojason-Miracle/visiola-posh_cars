# Generated by Django 3.2.23 on 2024-05-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poshcars', '0002_auto_20240508_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='rental_price_per_day',
            field=models.PositiveIntegerField(),
        ),
    ]
