from django.urls import path
from .views import home, register, loginView, cars,  user_dashboard, add_car,reviews, client_cars, Logout, carsDetails, Update, Delete, Rentcar, Rental_form, UserDetails




urlpatterns = [
    path('', home, name='home'),

    
    path('register', register, name='register'),
    
    path('userdetails', UserDetails, name='userdetails'),
    
     path('rentcarform', Rental_form, name='rentcarform'),

    
    path('login', loginView, name='login'),

  
    path('cars', cars, name='car_rental'),

  
    path('reviews', reviews, name='reviews'),

   
    path('user-dashboard', user_dashboard, name='user_dashboard'),
    
     
  path('rentcar/<int:car_id>/', Rentcar, name='rentcar'),

    
    path('add-car', add_car, name='add_car'),

  
    path('logout', Logout, name='logout'),

  
    path('client-cars', client_cars, name='client_cars'),
    
     path('details/<int:pid>', carsDetails, name='car-details'),
     
      path('delete/<int:pid>', Delete, name='delete'),
      
 path('update/<int:pid>', Update, name='update'),
]

