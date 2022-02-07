from django import forms 
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ReserveTableForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Your phone'}))
    number_of_persons = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Number of persons'}))
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = Reservation
        fields = '__all__'
        
