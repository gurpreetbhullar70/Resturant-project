from django import forms 
from .models import Reservation

class ReserveTableForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    number_of_persons = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control'}))
    class Meta:
        model = Reservation
        fields = '__all__'