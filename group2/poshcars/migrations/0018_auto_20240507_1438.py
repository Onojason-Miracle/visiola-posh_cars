# Generated by Django 3.2.23 on 2024-05-07 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poshcars', '0017_remove_car_mileage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='delivery_options',
        ),
        migrations.RemoveField(
            model_name='car',
            name='driver',
        ),
    ]
