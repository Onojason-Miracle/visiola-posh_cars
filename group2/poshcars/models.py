from django.db import models

class CarBrand(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name

class RentalAgency(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed
    
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
    rental_agency = models.ForeignKey(RentalAgency, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    number_of_doors = models.PositiveIntegerField()
    number_of_seats = models.PositiveIntegerField()
    rental_price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    availability_calendar = models.TextField()
    special_offers = models.TextField(blank=True)
    image = models.ImageField(upload_to='car_images/')
    air_conditioning = models.BooleanField(default=False)
    gps_navigation = models.BooleanField(default=False)
    bluetooth_connectivity = models.BooleanField(default=False)
    safety_features = models.TextField()
    audio_system_details = models.TextField()
    description = models.TextField()
    location = models.CharField(max_length=200)
    delivery_options = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.year} {self.brand.name} {self.model}"
