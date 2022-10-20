from smtplib import SMTPException
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings

import random
from .models import RestaurantAdmin, Restaurant
from user_app import models as user_models
from food_app.models import Food


def register_admin(data:dict):
    email:str = data.get('name').replace(' ','').lower()+str(random.randint(0,999))+'@bhoklagyo.com'
    phone:str = data.get('phone')
    passkey_raw:str = str(data.get('name').replace(' ',''))+str(phone)
    random_pass:str = ''.join(random.choices(passkey_raw,k=10))

    try:
        send_mail(
            subject='Your password for Bhoklagyo',
            message=f'Your password for Bhoklagyo with email {email} is {random_pass}.\
            Make sure you do not share it with anybody.',
            from_email=f'{settings.EMAIL_HOST_USER}',
            recipient_list=[f'bhattarais009@gmail.com'],
            fail_silently=False,
        )
        user:user_models.User = user_models.User.objects.create(
            email = email,
            phone = phone,
            password = make_password(random_pass),
            is_staff = True,
            role = user_models.User.RESTAURANT_ADMIN,
        )

        restaurant:Restaurant = Restaurant.objects.create(
            restaurant_name = data.get('name'),
            location = data.get('location'),
            phone = data.get('phone'),
            # pan = data.get('PAN')
        )
        admin:RestaurantAdmin = RestaurantAdmin.objects.create(
            user = user,
            email = email,
            restaurant=restaurant,
        ) 
    except Exception as e:
        return HttpResponse("Could not complete the process")
    
 
    

    
def register_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('restaurant_name','')
        location = request.POST.get('address','')
        phone = request.POST.get('phone','')
        pan = request.POST.get('pan','')
        # email = request.POST.get('email')
        data ={
            'name':name,
            'location':location,
            'phone':phone,
            'PAN':pan
        }
    
        register_admin(data)
        return redirect('login-restaurant')
    else:
        return render(request, 'restaurant_app/register.html')

def login_admin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        admin = authenticate(request, email=email, password=password, role=user_models.User.RESTAURANT_ADMIN)
        
        if admin:
            login(request, admin)
            return redirect('dashboard')
        else:
            message = messages.error(request, "Unable to login. Please input valid credentials.")
            return render(request, 'restaurant_app/login-admin.html',{'message':message})
    else:
        return render(request, 'restaurant_app/login-admin.html')
    
    
def logout_admin(request):
    logout(request)
    return redirect('login-restaurant')

def add_food(request):
    if request.method == 'POST':
        user = RestaurantAdmin.objects.get(user_id=request.user.id)
        print(f"{user=}")
        if user:
            name = request.POST.get('name')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            restaurant = Restaurant.objects.get(id=user.restaurant_id)
            print(f"{name=} {price=}")
            food = Food.objects.create(
                name = name,
                unit_price = price,
                image = image,
                restaurant_id = restaurant.id,
                image_url = f'media/images/{image}',
                slug = restaurant.restaurant_name.replace(' ','-').lower()+'-'+name.replace(' ','-').lower() 
            )
            return redirect('dashboard')
        else: 
            return redirect('login-restaurant')
    else:
        return redirect('dashboard')

# modified by shantosh upload by ashant for restaurant admin panel
def dashboard(request):
    restaurant_id=RestaurantAdmin.objects.get(user_id=request.user.id).restaurant_id
    foods = Food.objects.filter(restaurant_id=restaurant_id)
    return render(request, 'restaurant_app/admin-panel.html', {'foods':foods})
