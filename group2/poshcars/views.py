from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone

# to do registration amd login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from .forms import CarForm, UpdateCar
from .models import Car, Rental

# Create your views here.

def home(request):
    return render(request, 'poshcars/home.html')

def cars(request):
    allcars = Car.objects.all()
    return render (request, 'poshcars/cars.html', {'allcars':allcars})


def carsDetails(request, pid):
    details = Car.objects.get(id=pid)
    return render(request, 'poshcars/cardetails.html', {'posts':details})

def Update(request, pid):
    post = get_object_or_404(Car, id=pid)
    if request.method == "POST":
        form = UpdateCar(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('car_rental')
    else:
        form = UpdateCar(instance=post)
        
    return render(request, 'poshcars/update.html',{'post':post, 'form':form})


def Delete(request, pid):
    caritem = get_object_or_404(Car, id=pid)
    if request.method == "POST":
         caritem.delete()
         return redirect('car_rental')
    return render(request,'poshcars/delete.html', {'caritem':caritem})

def reviews(request):
    return render(request, 'poshcars/reviews.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get("f-name").capitalize()
        last_name = request.POST.get("l-name").capitalize()
        email = request.POST.get('email')
        nin = request.POST.get('nin')
        phone_number = request.POST.get('phonenumber')
        d_license = request.POST.get('drivers_license')
        password = request.POST.get("password")
        c_password = request.POST.get("c-password")
        
        if User.objects.filter(email=email).exists():
            return render(request, "poshcars/register.html", {"error": 'sorry email already Exists'})
    
        if password != c_password:
            return render(request, "poshcars/register.html", {"error": 'sorry password does not match'})
    
        # creating the user

        user = User(email = email, first_name = first_name, last_name = last_name,username=email,  password = make_password(password))

        user.save()
        return redirect('login')
        
    return render(request, 'poshcars/register.html')

def loginView(request):
    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = email, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect ('user_dashboard')
            else:
                return render(request, 'poshcars/login.html', {'error': 'sorry this user is not active'})
        
        else:
            return render(request, 'poshcars/login.html', {'error': 'invalid user details, user does not exist'})
    
    return render(request, 'poshcars/login.html')

def Rentcar(request,car_id):
    rent = Car.objects.get(id=car_id)
    return render(request, "poshcars/rentcar.html", {"posts": rent,'id':car_id})



def Rental_form(request):
    if request.method == 'POST':
        print("we are here")
        duration = request.POST.get('duration')
        quantity = request.POST.get('quantity')
        payment_method = request.POST.get('payment_method')
        
        carId = request.POST.get('car')
        try:
            currentCar = Car.objects.get(id=int(carId))
            rental = Rental(duration=duration, quantity=quantity, payment_method=payment_method,
            user = request.user,
            car=currentCar,
            enddate = timezone.now() + timezone.timedelta(days=int(duration)))
            rental.save()
            
            # Adding a success message for the users
            messages.success(request, 'Form submitted successfully!')
        except Car.DoesNotExist:
            return render(request, 'poshcars/rentcar.html',{"msg":"car does not exist"})
            
        
        
        # Redirect to the user dashboard
        return redirect('user_dashboard')
    
    # If the request method is not POST, render the form
    return render(request, 'poshcars/rentcar.html')


def add_car(request):
    if request.method == "POST":
        my_form = CarForm(request.POST, request.FILES) 
        if my_form.is_valid():
            my_form.save()
            return redirect('car_rental')
    else:
        my_form = CarForm()  

    return render(request, 'poshcars/addcars.html', {"form": my_form})  

def user_dashboard(request):
    userrental = Rental.objects.filter(user = request.user)
    return render(request, 'poshcars/dashboard.html', {'userrental':userrental})

def Logout(request):
    logout(request)
    return redirect('login')

def client_cars(request):
    if request.method=='POST':
        form = RentalAuthForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print (form.errors)
    else:
        form = RentalAuthForm
        # return("error")

    return render(request, 'poshcars/clientcars.html',{'form_key': form})

