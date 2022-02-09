from django.shortcuts import render,redirect
from django.http import  HttpResponse
import reservation
from .models import *
from .forms import ReservationForm

def reserve_table(request):
    orders = Reservation.objects.all()
    customers = Customer.objects.all()
    
    context = {
        'orders' : orders,
        'customers' : customers,
        
    }
    
    
    return render(request, 'Reservation/reservation.html', context)



    


        
def customer_table(request, pk):
    
    
    pp = Reservation.objects.filter(id=pk)
    
    
    
    context = {
        
        'pp' : pp,
        
        }
    return render(request, 'Reservation/view_reservation.html', context)
        

    
def create_order(request):
    form = ReservationForm()
    if request.method == 'POST':
        
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reserve_table/')
        
    
    context = {
        'form' : form,
    }
    return render(request, 'Reservation/create_reservation.html', context)



def update_order(request, pk):
    
    order = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=order)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/reserve_table/')
    context = {
        'form' : form,
    }
    return render(request, 'Reservation/update_reservation.html', context)



def delete_order(request, pk):
    order = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/reserve_table/')
    context = {
        'item' : order,
        
    }
    return render(request, 'Reservation/delete_reservation.html', context)
    

    