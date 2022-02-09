from django.forms import ModelForm 
from .models import Reservation


# class DateInput(ModelForm .DateInput):
#     input_type = 'date'

# class TimeInput(ModelForm .TimeInput):
#     input_type = 'time'

class ReservationForm(ModelForm):
    # name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    # phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Your phone'}))
    # number_of_persons = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Number of persons'}))
    # date = ModelForm.DateField(widget=DateInput)
    # time = ModelForm.TimeField(widget=TimeInput)
    class Meta:
        model = Reservation
        fields = ['name', 'email','persons', 'time', 'date', 'phone']
         
