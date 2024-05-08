# Generated by Django 3.2.23 on 2024-05-08 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=20)),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=20)),
                ('number_of_doors', models.PositiveIntegerField()),
                ('number_of_seats', models.PositiveIntegerField()),
                ('rental_price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=200)),
                ('availability', models.BooleanField()),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField()),
                ('insurance', models.BooleanField()),
                ('verified', models.BooleanField(default=False)),
                ('plate_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nin', models.CharField(max_length=20)),
                ('phonenumber', models.IntegerField()),
                ('drivers_license', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('cash', 'Cash')], max_length=20)),
                ('startdate', models.DateField(default=django.utils.timezone.now)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poshcars.car')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poshcars.carbrand'),
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
