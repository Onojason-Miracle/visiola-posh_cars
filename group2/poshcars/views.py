from django.shortcuts import render,redirect

# to do registration amd login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

from .models import RentalAuth
from .forms import RentalAuthForm

# Create your views here.

def home(request):
    return render(request, 'poshcars/home.html')

def cars(request):
    return render(request, 'poshcars/cars.html')

def reviews(request):
    return render(request, 'poshcars/reviews.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get("f-name").capitalize()
        last_name = request.POST.get("l-name").capitalize()
        email = request.POST.get('email')
        password = request.POST.get("password")
        c_password = request.POST.get("c-password")
        
        if User.objects.filter(email=email).exists():
            return render(request, "poshcars/register.html", {"error": 'sorry email already Exists'})
    
        if password != c_password:
            return render(request, "poshcars/register.html", {"error": 'sorry password does not match'})
    
        # creating the user

        user = User(email = email, first_name = first_name, last_name = last_name, password = make_password(password))

        user.save()
        return redirect('login')
        
    return render(request, 'poshcars/register.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email = email, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect ('user_dashboard')
        else:
            return render(request, 'poshcars/login.html', {'error': 'sorry this user is not active'})
        
    else:
        return render(request, 'poshcars/login.html', {'error': 'invalid user details, user does not exist'})
    
    return render(request, 'poshcars/login.html')

def add_car(request):
    return render(request, 'poshcars/addcars.html')

def user_dashboard(request):
    return render(request, 'poshcars/dashbaord.html')

def Logout(request):
    logout(request)
    return redirect('login')

def client_cars(request):
    if request.method=='POST':
        form = RentalAuthForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client_cars')
    else:
        form = RentalAuthForm

    return render(request, 'poshcars/clientcars.html',{'form_key': form})