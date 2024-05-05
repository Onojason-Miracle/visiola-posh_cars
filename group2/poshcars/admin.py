from django.contrib import admin

from .models import CarBrand, Car,  RentalAuth

# Register your models here.

admin.site.register(CarBrand)
admin.site.register(Car)
admin.site.register(RentalAuth)

