#from .models import Contact
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings
# Create your views here.
#from contact.models import Contact


def send_email(request):
    if request.method == 'POST':
        
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(
                'From: ' + name, 
                'Message: ' + message, 
                'To' + email, 
                recipient_list,
                ['preet@gmail.com'],
                )
        
        
            messages.add_message(request, messages.SUCCESS, f" {name} ")

        return HttpResponseRedirect('/contact/')
    
    
    else:
        form = ContactForm()  
        
        context = {
            'form' : form
        } 
        return render(request, 'contact/contact.html', context)
    
    

        
                
            
        
        