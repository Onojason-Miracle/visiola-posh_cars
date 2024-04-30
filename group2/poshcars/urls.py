from django.urls import path
from .views import home, register, login, cars,  user_dashboard, add_car,reviews




urlpatterns = [
   path('', home, name='home'),
   
   #path for registration
   path('register', register, name='register'),
   
   #path for logging
   path('login', login, name='login'),
   
   # car listing
   path('cars', cars, name='car_rental'),
   
   # car listing
   path('reviews', reviews, name='reviews'),
   
    # user dashboard
   path('user_dashboard', user_dashboard, name='user_dashboard'),
   
   #add a new car to the database by clients bringing their cars for rent
    path('add_car', add_car, name='add_car'),

]