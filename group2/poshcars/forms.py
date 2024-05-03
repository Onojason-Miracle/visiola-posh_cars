from django import forms
from .models import RentalAuth

class RentalAuthForm(forms.ModelForm):
    class Meta:
        model = RentalAuth
        fields = '__all__'    