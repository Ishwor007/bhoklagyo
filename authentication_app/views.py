from pickle import FALSE
import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from user_app import views as user_view
from user_app.models import Customer, User


def send_otp_via_email(email):
    subject = "Your account verification email"
    otp = str(random.randint(100000,999999))
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message , email_from , [email])
    return otp

def validateOtp(request):
    valid_phone=False
    try:
        user_list=request.session["user_list"]
        first_name, last_name, email, phone, password, generatedotp = user_list[:6]
        # last_name = user_list[1]
        # email = user_list[2]
        # phone = user_list[3]
        # password = user_list[4]
        # generatedotp = user_list[5]
    except KeyError:
        return redirect('/')
    if request.method != "POST":  
        return render(request, 'authentication_app/otp.html')
    else:
        userotp = request.POST['otp']
        if generatedotp == userotp :
            user = Customer.objects.get_or_create(
                                    first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    password=password)
            
            # authenticate_user = authenticate(request, email = email, password =  password)
            # if authenticate_user:
            #     login(request, user)
            #     return redirect('/')
            return redirect(user_view.login_page)
        
        else:
            return HttpResponse("your otp is wrong")

        
def resend_otp(request):
    user_list = request.session['user_list']
    email = request.session.get('email')  
    print("----------------------------------") 
    print(user_list) 
    print("------------------------------")
    opt = send_otp_via_email(email)
    return redirect('otp')