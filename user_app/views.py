from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from authentication_app import views as auth_views
#from django.contrib.auth.models import login, authenticate
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def signup_page(request):
    return render(request,'user_app/signup.html')

def login_page(request):
    return render(request,'user_app/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        try:
            user = User.objects.get(phone=phone)
        except ObjectDoesNotExist:
            user=None
        print(user)
        if user: 
            message = messages.error(request, "User with provided info already exists.")
            return render(request,'user_app/signup.html',{'message':message})
        else:
            otp = auth_views.send_otp_via_email(email)
            user_list = [first_name,last_name,email,phone,password,otp]
            request.session["user_list"]=user_list
            return redirect(auth_views.validateOtp)
            
    else:
        return HttpResponse('signup')

def login_user(request):
    if request.method=='POST':
        phone = request.POST['phone']
        pass_key = request.POST['password']
        print(phone, pass_key)

        user = User.objects.get(phone=phone)
        if user:
            password = user.password
            if check_password(pass_key, password):
                return HttpResponse(password)
            else:
                return HttpResponse("suck")
            # login(request, user)
        else:
            return HttpResponse("user not found")

