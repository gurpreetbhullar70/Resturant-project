from django.contrib import admin
from .models import Customer, Table, Reservation


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'full_name', 'email')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_name', 'max_no_people')


@admin.register(Reservation)
class ReservationsAdmim(admin.ModelAdmin):
    list_filter = ('no_of_guests', 'table_id')
    list_display = ('customer', 'no_of_guests',
                    'table', 'requested_date')