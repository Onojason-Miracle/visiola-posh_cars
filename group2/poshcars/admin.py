from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CarBrand, Car,  RentalAuth, Rental, Userdetails

# Register your models here.

admin.site.register(CarBrand)
admin.site.register(Car)
admin.site.register(RentalAuth)
admin.site.register(Rental)
admin.site.register(Userdetails)


