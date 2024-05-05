from django import forms
from .models import Car, CarBrand, RentalAuth

class RentalAuthForm(forms.ModelForm):
    class Meta:
        model = RentalAuth
        fields = '__all__'    
        
        
        
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'   
        widgets = {
            'transmission': forms.Select(choices=Car.TRANSMISSION_CHOICES),
            'fuel_type': forms.Select(choices=Car.FUEL_CHOICES),
            'availability': forms.Select(choices=[(False, 'No'), (True, 'Yes')]),

            
            'delivery_options': forms.Select(choices=[(False, 'No'), (True, 'Yes')]),
            'driver': forms.Select(choices=[(False, 'No'), (True, 'Yes')]),
            # Add more widgets for other fields as needed
        }
        
        
        
class UpdateCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"