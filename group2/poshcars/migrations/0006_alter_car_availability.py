# Generated by Django 3.2.23 on 2024-05-08 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poshcars', '0005_rental_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='availability',
            field=models.BooleanField(default=False, null=True),
        ),
    ]