from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import  Car, Rental, Userdetails

# Register your models here.


admin.site.register(Car)
admin.site.register(Rental)
admin.site.register(Userdetails)


