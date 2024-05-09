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
    user = request.user
    allcars = Car.objects.filter(verified=True)
    returned = Rental.objects.filter(is_returned = False)
    return render (request, 'poshcars/cars.html', {'allcars':allcars, 'user':user, 'returned':returned})

def carsDetails(request, pid):
    details = Car.objects.get(id=pid)
    return render(request, 'poshcars/cardetails.html', {'posts':details})





def Update(request, car_id):
    
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
       
        car.brand = request.POST.get('brand').capitalize()
        car.model = request.POST.get('model').capitalize()
        car.year = request.POST.get('year')
        car.color = request.POST.get('color')
        car.transmission = request.POST.get('transmission')
        car.fuel_type = request.POST.get('fuel_type')
        car.number_of_doors = request.POST.get('number_of_doors')
        car.number_of_seats = request.POST.get('number_of_seats')
        car.rental_price_per_day = request.POST.get('rental_price_per_day')
        car.location = request.POST.get('location').capitalize()
        car.availability = request.POST.get('availability')
        car.insurance = request.POST.get('insurance')
        car.plate_number = request.POST.get('plate_number')
        if request.FILES.get('image'):
            car.image = request.FILES.get('image')
        
        car.save()
        messages.success(request, 'Update of car successful')
      
        return redirect('car_rental')

   
    return render(request, 'poshcars/update.html', {'car': car})





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
        
        if User.objects.filter(username=email).exists():
            return render(request, "poshcars/register.html", {"emailerror": 'email already Exists'})
    
        if password != c_password:
            return render(request, "poshcars/register.html", {"pswderror": 'password does not match'})
    
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

def Rentcar(request,car_id):
    rent = Car.objects.get(id=car_id)
    return render(request, "poshcars/rentcar.html", {"posts": rent,'id':car_id})




def Rental_form(request):
    if request.method == 'POST':
        print("we are here")
        duration = int(request.POST.get('duration'))
        payment_method = request.POST.get('payment_method')
        
        carId = request.POST.get('car')
        try:
            currentCar = Car.objects.get(id=int(carId))
            rental = Rental(duration=duration, payment_method=payment_method,
            user = request.user,
            car=currentCar,
            totalPrice = currentCar.rental_price_per_day * duration,
            enddate = timezone.now() + timezone.timedelta(days=int(duration)))
            
            rental.save()
            
          
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
    if request.user.is_superuser:
        unverified_cars = Car.objects.filter(verified=False)

        unapproved_rent = Rental.objects.filter(is_approved=False)
        returned_car = Rental.objects.filter(is_returned=False)
    
        rents_with_users = []
        for rent in unapproved_rent:
            user = rent.user
            rents_with_users.append((rent, user))
        
        return render(request, 'poshcars/dashboard.html', { 'unverified_cars':unverified_cars,'unverified_rent':unapproved_rent,
        'returned_car':returned_car, 
         
        'rents_with_users': rents_with_users                                                
                                                           
        })
        
    else:
          userrental = Rental.objects.filter(user=request.user)
          return render(request, 'poshcars/dashboard.html',{'userrental':userrental,})
    
    
def approved_rent(request,id):
    if request.user.is_superuser:
        car_approved = Rental.objects.get(id=id)
        if car_approved.is_approved:
            return 'Car already approved'
        car_approved.is_approved = True
        car_approved.save(update_fields=['is_approved'])
        
        
        return redirect('user_dashboard', {"success":'car approved successfully'})
    
    # if not admin
    return redirect('user_dashboard')



def is_returned(request,id):
    if request.user.is_superuser:
        car_returned = Rental.objects.get(id=id)
        
        
        if car_returned.is_returned:
            return 'car retured'
        car_returned.is_returned = True
        car_returned.save(update_fields=['is_returned'])
        return redirect('user_dashboard')
    
    # if not admin
    return redirect('user_dashboard')

def Logout(request):
    logout(request)
    return redirect('login')


def UpdateUserDetails(request, pid):
    userdetail = get_object_or_404(Userdetails,id=pid)
    if request.method == "POST":
        userdetail.user = request.POST.get('user').capitalize()
       
        userdetail.nin = request.POST.get('nin')
        userdetail.phone = request.POST.get('phonenumber')
        userdetail.drivers_license = request.POST.get('drivers_license')
       
        if request.FILES.get('image'):
            userdetail.image = request.FILES.get('image')

        
        userdetail.save()
        
        return redirect('user_dashboard')
    return render(request, 'poshcars/update-userdetails.html', {'userdetails': userdetail})






def verify_car(request,vid):
    if request.user.is_superuser:
        car = Car.objects.get(id=vid)
        car.verified = True
        
        car.save()
       
        return redirect('car_rental')
    
    # if not admin
    return redirect('car_rental')