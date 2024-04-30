from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'poshcars/home.html')

def cars(request):
    return render(request, 'poshcars/cars.html')

def reviews(request):
    return render(request, 'poshcars/reviews.html')

def register(request):
    return render(request, 'poshcars/registere.html')

def login(request):
    return render(request, 'poshcars/login.html')

def add_car(request):
    return render(request, 'poshcars/clientcars.html')

def user_dashboard(request):
    return render(request, 'poshcars/dashbaord.html')
