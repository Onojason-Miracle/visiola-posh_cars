from django.urls import path
from .views import home, register, login, cars,  user_dashboard, add_car,reviews, external_car, Logout




urlpatterns = [
   path('', home, name='home'),
   
   #path for registration/creating an account
   path('register', register, name='register'),
   
   #path for logging
   path('login', login, name='login'),
   
   # car listing
   path('cars', cars, name='car_rental'),
   
   # car listing
   path('reviews', reviews, name='reviews'),
   
    # user dashboard
   path('user_dashboard', user_dashboard, name='user_dashboard'),
   
   #add a new car to the database by the super user  for rent
    path('add_car', add_car, name='add_car'),
    
    #add a new car to the database by clients bringing their cars for rent
    path('external_car', external_car, name='external_car'),

    #user logout
    path('logout', Logout, name='logout'),
]