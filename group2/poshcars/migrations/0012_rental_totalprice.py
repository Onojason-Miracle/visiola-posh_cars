# Generated by Django 3.2.23 on 2024-05-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poshcars', '0011_alter_car_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='totalPrice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
