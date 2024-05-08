from django.urls import path
from .views import home, register, loginView, cars,  user_dashboard, add_car,reviews, Logout, carsDetails, Update, Delete, Rentcar, Rental_form, UserDetail, UpdateUserDetails, Submitcar, verify_car




urlpatterns = [
    path('', home, name='home'),
    
    path('successful', Submitcar, name='successful'),
    
    path('register', register, name='register'),
    
    path('userdetails', UserDetail, name='userdetails'),
    
    path('rentcarform', Rental_form, name='rentcarform'),

    
    path('login', loginView, name='login'),

  
    path('cars', cars, name='car_rental'),

  
    path('reviews', reviews, name='reviews'),

    path('user-dashboard', user_dashboard, name='user_dashboard'),
    
  path('rentcar/<int:car_id>/', Rentcar, name='rentcar'),

    
    path('add-car', add_car, name='add_car'),

  
    path('logout', Logout, name='logout'),

  
    
    path('details/<int:pid>', carsDetails, name='car-details'),
    
    path('delete/<int:pid>', Delete, name='delete'),
      
    path('update/<int:pid>', Update, name='update'),

    path('update-userdetails/<int:pid>', UpdateUserDetails, name='updateUserDetails'),
    path('verify-car/<int:id>',verify_car, name="verify-car")
]

