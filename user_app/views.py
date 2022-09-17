from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist


from authentication_app import views as auth_views
from .models import Customer,User

# Create your views here.

def signup_page(request):
    return render(request,'user_app/signup.html')

def login_page(request):
    return render(request,'user_app/login.html')

def register_customer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password =make_password(request.POST['password'])
        try:
            user = User.objects.get(phone=phone)
        except ObjectDoesNotExist:
            user=None

        if user:
            message = messages.error(request, "User with provided phone number already exists.")
            return render(request,'user_app/signup.html',{'message':message})
        else:
            otp = auth_views.send_otp_via_email(email)
            user_list = [first_name,last_name,email,phone,password,otp]
            request.session["user_list"]=user_list
            return redirect(auth_views.validateOtp)
            
    else:
        return redirect('signup')



def login_user(request):
    if request.method=='POST':
        phone = request.POST['phone']
        pass_key = request.POST['password']
        user = authenticate(phone=phone, password=pass_key)
        
        if user and user.role == User.CUSTOMER:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('landing_page')
        else:
            return HttpResponse(f"Oops! This user does not exist")


def logout_user(request):
    logout(request)
    return redirect('login')
