from email import message
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.http import  HttpResponse,HttpResponseRedirect
import reservation
from .models import *
from .forms import ReservationForm, CustomerForm, CreateUserForm
import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Table, Customer, Reservation
from django.conf import settings
from django.views import View
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

#@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            
            messages.success(request, 'Account was created for ' + username)
            
            return redirect('/reserve_table/login')
            
    context = {
        'form' : form,
    }
    return render(request, 'Reservation/register.html', context)


#@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password incorrect')
            
    context = {}
    return render(request, 'Reservation/login.html', context)




def logoutUser(request):
    logout(request)
    return redirect('/reserve_table/login')











def check_availabilty(customer_requested_time, customer_requested_date):
    """ check availability against Reservation model using customer input """

    # Check to see how many bookings exist at that time/date
    no_tables_booked = len(Reservation.objects.filter(
        time=customer_requested_time,
        date=customer_requested_date, status="confirmed"))

    # Return number of tables
    return no_tables_booked




def get_customer_instance(request, User):
    """ Returns customer instance if User is logged in """
    customer_email = request.user.email
    customer = Customer.objects.filter(email=customer_email).first()

    return customer







def get_tables_info():
    """ Retrieves the number of tables in the table model """
    max_tables = len(Table.objects.all())

    return max_tables








@login_required(login_url='/reserve_table/login')
@allowed_users(allowed_roles=['customer'])
def create_order(request, User=User, *args, **kwargs):
    
    form = ReservationForm()
    customer_form = CustomerForm()
            
    if request.method == 'POST':
        # Get post data from forms
        customer_form = CustomerForm(data=request.POST)
        form = ReservationForm(data=request.POST)

        if customer_form.is_valid() and form.is_valid():
            # Retreive information from forms
            customer_requested_date = request.POST.get('date')
            customer_requested_time = request.POST.get('time')
            customer_requested_guests = request.POST.get('persons')
            customer_name = request.POST.get('name')

            # Convert date in to format required by django
            date_formatted =  date_formatted =  datetime.datetime.strptime(
                    customer_requested_date, "%Y-%m-%d")

            # Check to see how many bookings exist at that time/date
            tables_booked = check_availabilty(
                customer_requested_time, date_formatted)

            # Get the number of tables in the restaurant
            max_tables = get_tables_info()

            # Compare number of bookings to number of tables available
            if tables_booked >= max_tables:
                """ If the number of tables is bigger than or equal to the
                max number of tables in the restaurant stop form being
                submitted
                """
                messages.add_message(
                    request, messages.ERROR,
                    "Unfortunately we are fully booked at "
                    f"{customer_requested_time} on {customer_requested_date}.")
                
                #return HttpResponseRedirect('/reserve_table/create_order/')
                return render(request, 'Reservation/create_reservation.html',
                                {'customer_form': customer_form,
                                 'form': form})

            else:
               
                    customer_formss=customer_form.save(commit=False)
                    customer_formss.manger = request.user
                    customer_formss.save()

                # Retreive customer information to pass to reservation model
              

                    reservations = form.save(commit=False)
                    
                    # Pass formatted date & customer in to model
                    reservations.date = date_formatted
                    
                
                    #Save reservation
                    form.save()

                    messages.add_message(
                            request, messages.SUCCESS,
                            f"Thank you {customer_name}, your enquiry for "
                            f"{customer_requested_guests} people at "
                            f"{customer_requested_time} on "
                            f"{customer_requested_date} has been sent.")

                    # Return blank forms so the same enquiry isn't sent twice.
                
                    return HttpResponseRedirect('/reserve_table/create_order/')


    return render(request, 'Reservation/create_reservation.html',
                    {'customer_form': customer_form,
                    'form': form})








@login_required(login_url='/reserve_table/login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    
    order = Reservation.objects.filter(manger__id=request.user.id)
    
    
        
        
           
                        
            
            
    
    #customers = Reservation.objects.filter(customer__id=request.customer.id)
    
    print('ORDERS', order)
    context = {}
    context['order']=order
    return render(request,'Reservation/users.html', context)









# def retrieve_reservations(request, User):
#     """ Get any existing reservations for the customer in the
#     Reservation model. If there are no reservations then redirect
#     customer to Reservations page.
#     """
#     customer_email = request.user.email
#     if len(Customer.objects.filter(email=customer_email)) != 0:
#         # If customer exists in model
#         current_customer = Customer.objects.get(email=customer_email)
#         current_customer_id = current_customer.id

#         # Get any reservations using the customer instance
#         get_reservations = Reservation.objects.filter(
#             customer=current_customer_id).values().order_by('date')

#         if len(get_reservations) == 0:
#             # if no reservations
#             return None
#         else:
#             return get_reservations
#     else:
#         # if user is not present in customer model
#         return None



# def validate_date(request, reservations):
#     today = datetime.datetime.now().date()
#     for reservation in reservations:
#         if reservation['date'] < today:
#             reservation['status'] = 'expired'

#         return reservations










# def create_order(request):
#     form = ReservationForm()
#     customer_form = CustomerForm()
#     if request.method == 'POST':
        
#         form = ReservationForm(request.POST)
#         customer_form = CustomerForm(request.POST)
#         if form.is_valid() and customer_form.is_valid():
           
                        
            
#             form.save() and customer_form.save()
#             return redirect('/reserve_table/')
        
    
#     context = {
#         'form' : form,
#         'customer_form': customer_form,
#     }
#     return render(request, 'Reservation/create_reservation.html', context)






















@login_required(login_url='/reserve_table/login')
@admin_only
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
        









def update_order(request, pk):
    
    order = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=order)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            
            messages.add_message(request, messages.SUCCESS,f'thnx')
            
            return HttpResponseRedirect('/reserve_table/')
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
    
  
  
  
