# Generated by Django 3.2.23 on 2024-05-07 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poshcars', '0009_auto_20240507_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='startdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]