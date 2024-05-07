from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CarBrand(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name
    

    
    
class RentalAuth(models.Model):
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=50 , unique=True)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    year_of_manufacture = models.IntegerField()
    milleage = models.FloatField()
    nin = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    number_of_seats = models.IntegerField()
    number_of_doors = models.IntegerField()
    car_reg_number = models.CharField(max_length=50)
    daily_rental_rate = models.FloatField()
    insurance = models.CharField(max_length=50)
    car_image = models.ImageField(upload_to='media')
    transmission_type = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
   

    def __str__(self):
        return self.name

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    
  
    
  

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    rental_agency = models.ForeignKey(RentalAuth, on_delete=models.CASCADE)
    
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    number_of_doors = models.PositiveIntegerField()
    number_of_seats = models.PositiveIntegerField()
    rental_price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    delivery_options =  models.BooleanField()
    driver = models.BooleanField()
    availability = models.BooleanField() 
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    
    
    def __str__(self):
        return f"{self.brand.name} {self.model}"
    
    
    
    
class Rental(models.Model):
   
    
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('cash', 'Cash'),
        
    ]
    
   
    duration = models.IntegerField()
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True )
    car = models.ForeignKey(Car,on_delete=models.CASCADE,blank=True, null=True )
    startdate = models.DateField(default=timezone.now,)
    enddate = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.quantity} cars rented for with {self.payment_method}"




# class CustomUser(AbstractUser):
#     nin = models.CharField(max_length=20,)
#     phonenumber = models.IntegerField()
#     drivers_license = models.CharField(max_length=20)
#     email = models.CharField(max_length=50, unique=True)

#     REQUIRED_FIELDS = [ 'nin', 'phonenumber', 'drivers_license']
#     USERNAME_FIELD = 'email'






