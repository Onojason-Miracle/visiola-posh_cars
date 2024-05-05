from django.urls import path
from .views import home, register, loginView, cars,  user_dashboard, add_car,reviews, client_cars, Logout, carsDetails, Update, Delete




urlpatterns = [
    path('', home, name='home'),

    #path for registration/creating an account
    path('register', register, name='register'),

    #path for logging
    path('login', loginView, name='login'),

    # car listing
    path('cars', cars, name='car_rental'),

    # car listing
    path('reviews', reviews, name='reviews'),

    # user dashboard
    path('user-dashboard', user_dashboard, name='user_dashboard'),

    #add a new car to the database by the super user  for rent
    path('add-car', add_car, name='add_car'),

    #user logout
    path('logout', Logout, name='logout'),

    #add a new car to the database by clients bringing their cars for rent
    path('client-cars', client_cars, name='client_cars'),
    
     path('details/<int:pid>', carsDetails, name='car-details'),
     
      path('delete/<int:pid>', Delete, name='delete'),
      
 path('update/<int:pid>', Update, name='update'),
]

