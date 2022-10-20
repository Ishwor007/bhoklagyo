from django.shortcuts import render
from django.http import HttpResponse
from .models import Food
from user_app.models import Customer
from order_app.models import Order

def landing_page(request):
    return render(request, 'food_app/index.html')

def home_page(request):
    foods = Food.objects.all()
    return render(request, 'food_app/foods.html', {'foods': foods})

def rate_food(request, id:int):
    user = request.user
    customer = Customer.objects.get(user_id=user)
    return HttpResponse("df")




