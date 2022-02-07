from django import forms 
#from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}))
    
