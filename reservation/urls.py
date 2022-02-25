from django.urls import path
from . import views


app_name = 'reservation'

urlpatterns = [
    
    
   
    
    path('', views.reserve_table, name='reserve_table'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user-page'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
    path('<str:pk>/', views.customer_table, name='customer_table'),
    
    
    
    
    
    

]