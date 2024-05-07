from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CarBrand, Car,  RentalAuth, Rental

# Register your models here.

admin.site.register(CarBrand)
admin.site.register(Car)
admin.site.register(RentalAuth)
admin.site.register(Rental)

