from django.db import models

# Create your models here.


# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     password = models.CharField(max_length=128)  # Add password field

class RentalAuth(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=50)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    year_of_manufacture = models.IntegerField()
    milleage = models.FloatField()
    fuel_type = models.CharField(max_length=50)
    number_of_seats = models.IntegerField()
    number_of_doors = models.IntegerField()
    car_reg_number = models.CharField(max_length=50)
    daily_rental_rate = models.FloatField()
    insurance = models.CharField(max_length=50)
    car_image = models.ImageField(upload_to='media')
    transmission_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name