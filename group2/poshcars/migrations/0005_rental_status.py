# Generated by Django 3.2.23 on 2024-05-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poshcars', '0004_auto_20240508_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]