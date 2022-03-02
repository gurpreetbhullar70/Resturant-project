#from django.forms import ModelForm 
import email
from django import forms
from .models import Reservation, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

class DateInput(forms.DateInput):
     input_type = 'date'



class CustomerForm(forms.ModelForm):
    
    phone = forms.CharField(widget=forms.TextInput(
    attrs={'placeholder': ('Please enter in +44 format')}))

    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone')
        



class ReservationForm(forms.ModelForm):
    
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Reservation
        fields = ['persons', 'time', 'date']
       




class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2' ]