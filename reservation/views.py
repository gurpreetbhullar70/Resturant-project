from .models import Reservation
from django.shortcuts import render
from .forms import ReserveTableForm
from django.http import  HttpResponseRedirect
from django.contrib import messages

from reservation.models import Reservation

def reserve_table(request):
    reserve_form = ReserveTableForm()
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        
        if reserve_form.is_valid():
            reserve_form.save() 
            
            messages.add_message(request, messages.SUCCESS, f" hello ")

        return HttpResponseRedirect('/reserve_table/')
            
    context = {'form': reserve_form }
    
    return render(request, 'Reservation/reservation.html', context)
            
    