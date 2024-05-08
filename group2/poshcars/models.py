from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




# model for Userdetails 
class  Userdetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nin = models.CharField(max_length=20,)
    
    phonenumber = models.IntegerField()
    
    drivers_license = models.CharField(max_length=20)
    
    image = models.ImageField(upload_to='media', blank=True, null=True)
    
    
    
# model for Car
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
    
  
    
  

    brand = models.CharField(max_length=50) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    number_of_doors = models.PositiveIntegerField()
    number_of_seats = models.PositiveIntegerField()
    rental_price_per_day = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    availability = models.BooleanField(null=True) 
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    insurance = models.BooleanField()
    verified = models.BooleanField(default=False, null=True)
    plate_number= models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return f"{self.brand} {self.model}"
    
    
    
 # model for Rental   
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
    status = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return f"{self.quantity} cars rented for with {self.payment_method}"










