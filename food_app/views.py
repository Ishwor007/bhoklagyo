from django.shortcuts import render

from .models import Food
from user_app.models import Customer

def landing_page(request):
    return render(request, 'food_app/index.html')

def home_page(request):
    foods = Food.objects.all()
    return render(request, 'food_app/foods.html', {'foods': foods})






