from tkinter import Widget
from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=20, null=True)
   
    
    def __str__(self):
        return self.name
    
    
    
class Table(models.Model):
   
    
    table_name = models.CharField(max_length=10, default="New table", unique=True)
    max_no_people = models.IntegerField()

    def __str__(self):
        return self.table_name


class Reservation(models.Model):
  
    
    STATUS = (("pending", "pending"),
                      ("confirmed", "confirmed"),
                      ("rejected", "rejected"),
                      ("expired", "expired"))

    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name="customer", null=True)
    guests_choices = ((1, "1 person"), (2, "2 people"),
                      (3, "3 people"), (4, "4 people"))
    persons = models.IntegerField(choices=guests_choices, default=1)
    date = models.DateField(default='2022-01-28')
    time = models.CharField(max_length=10, default='12:00')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, related_name="table_booked",null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='pending')
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.customer)


