# Generated by Django 3.2.23 on 2024-05-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poshcars', '0003_alter_car_rental_price_per_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='availability',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
