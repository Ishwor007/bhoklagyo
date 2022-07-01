from django.shortcuts import render

from restaurant_app.models import RestaurantAdmin, Restaurant

def register_restaurant(request):
    return render(request, 'restaurant_app/register.html') 


def register_admin(request):
    return render(request, 'restaurant_app/login-admin.html')

def login_admin(request):
    return render(request, 'restaurant_app/login-admin.html')
