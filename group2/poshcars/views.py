from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone

# to do registration amd login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from .models import Car, Rental, Userdetails

# Create your views here.

def home(request):
    return render(request, 'poshcars/home.html')

def cars(request):
    allcars = Car.objects.filter(verified=True)
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

def UserDetail(request):
    if request.method == 'POST':
        user = request.user
        
        nin = request.POST.get('nin')
        
        phonenumber = request.POST.get('phonenumber')
        
        drivers_license = request.POST.get('drivers_license')
        
        image = request.FILES.get('image')
        
        details = Userdetails(user=user, nin=nin, phonenumber=phonenumber,drivers_license=drivers_license, image=image )
        
        details.save()
        return redirect('user_dashboard')
    
    return render(request, 'poshcars/userdetails.html')

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

# def Rentcar(request,car_id):
#     rent = Car.objects.get(id=car_id)
#     return render(request, "poshcars/rentcar.html", {"posts": rent,'id':car_id})






def Rentcar(request, car_id):
    if request.method == 'POST':
        rent = Car.objects.get(id=car_id)
        duration = int(request.POST.get('duration'))
        quantity = int(request.POST.get('quantity'))

        # Calculate total price
        total_price = rent.rental_price_per_day * duration * quantity

        # Pass total price to the template
        return render(request, "poshcars/rentcar.html", {"posts": rent, 'id': car_id, 'total_price': total_price})
    else:
        rent = Car.objects.get(id=car_id)
        return render(request, "poshcars/rentcar.html", {"posts": rent, 'id': car_id})



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

def Submitcar(request):
    return render(request, 'poshcars/submitted.html')

def add_car(request):
    if request.method=='POST':
        carBrand = request.POST.get('brand').capitalize()
        car_model = request.POST.get('model').capitalize()
        year = request.POST.get('year')
        color = request.POST.get('color')
        transmission = request.POST.get('transmission')
        fuel_type = request.POST.get('fuel_type')
        number_of_seats = request.POST.get('number_of_seats')
        number_of_doors = request.POST.get('number_of_doors')
        rental_price_per_day = request.POST.get('rental_price_per_day')
        insurance = request.POST.get('insurance')
        image = request.FILES.get('image')
        location = request.POST.get('location').capitalize()
        plate_number = request.POST.get('plate_number')
        availability = request.POST.get('availability')
        description = request.POST.get('description')
        verified = request.POST.get('verified')
        user = request.user

        items = Car( brand = carBrand, model = car_model, year = year, color = color, transmission = transmission, fuel_type = fuel_type, number_of_seats = number_of_seats, number_of_doors = number_of_doors, rental_price_per_day=rental_price_per_day, insurance=insurance, image = image, location = location, plate_number= plate_number, availability = availability, description = description, verified = verified, user = user)
        
        items.save() 
        return redirect('successful')
    return render(request, 'poshcars/addcars.html') 

    

def user_dashboard(request):
    unverified_cars = Car.objects.filter(verified=False)
    unverified_rent = Rental.objects.filter(verified=False)
    unavailable_cars = Car.objects.filter(availability = False)
    userrental = Rental.objects.filter(user = request.user)
    return render(request, 'poshcars/dashboard.html', {'userrental':userrental, 'unverified_cars':unverified_cars,'unavailable_cars':unavailable_cars, 'unverified_rent':unverified_rent
    })

def Logout(request):
    logout(request)
    return redirect('login')

def client_cars(request):
    if request.method=='POST':
        car_make = request.POST.get('car_make')
        car_model = request.POST.get('car_model')
        year_of_manufacture = request.POST.get('year_of_manufacture')
        fuel_type = request.POST.get('fuel_type')
        number_of_seats = request.POST.get('number_of_seats')
        number_of_doors = request.POST.get('number_of_doors')
        daily_rental_rate = request.POST.get('daily_rental_rate')
        insurance_details = request.POST.get('insurance_details')
        photos = request.FILES.get('photos')
        car_reg_number = request.POST.get('car_reg_number')
        transmission = request.POST.get('transmission')
        user = request.user

        items = RentalAuth(car_make=car_make, car_model=car_model, year_of_manufacture=year_of_manufacture,fuel_type=fuel_type, number_of_seats=number_of_seats, number_of_doors=number_of_doors,
        car_reg_number =car_reg_number,daily_rental_rate=daily_rental_rate, insurance_details=insurance_details, photos=photos, transmission=transmission, user=user)
        items.save()
        return render(request, 'poshcars/submitted.html', {'items': items})
    return render(request, 'poshcars/clientcars.html')

def UpdateUserDetails(request, pid):
    userdetail = get_object_or_404(Userdetails,id=pid)
    if request.method == "POST":
        user = request.user
        nin = request.POST.get('nin')
        phonenumber = request.POST.get('phonenumber')
        drivers_license = request.POST.get('drivers_license')
        image = request.FILES.get('image')

        userdetail.user = user
        userdetail.nin = nin
        userdetail.phonenumber = phonenumber
        userdetail.drivers_license = drivers_license
        userdetail.image = image
        userdetail.save()
        return redirect('user_dashboard')
    return render(request, 'poshcars/update-userdetails.html', {'userdetails': userdetail})


def verify_car(request,id):
    if request.user.is_superuser:
        car = Car.objects.get(id=id)
        car.verified = True
        car.availability = True
        car.save()
        
        return redirect('car_rental')
    
    # if not admin
    return redirect('car_rental')