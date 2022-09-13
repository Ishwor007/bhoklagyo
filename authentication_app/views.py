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
    try:
        user_list=request.session["user_list"]
        first_name, last_name, email, phone, password, generatedotp = user_list[:6]

    except KeyError:
        return redirect('/')
    if request.method != "POST":  
        return render(request, 'authentication_app/otp.html')
    else:
        userotp = request.POST['otp']
        if generatedotp == userotp :
            user = User.objects.get_or_create(
                                    email=email,
                                    phone=phone,
                                    password=password
                                    )
            
            customer = Customer.objects.create(
                user=user[0],
                first_name=first_name,
                last_name=last_name,
                user_id = user[0].id
            )
            return redirect(user_view.login_page)
        
        else:
            return HttpResponse("your otp is wrong")

        
def resend_otp(request):
    user_list = request.session['user_list']
    email = request.session.get('email')  
    print("----------------------------------") 
    print(user_list) 
    print("------------------------------")
    send_otp_via_email(email)
    return redirect('otp')