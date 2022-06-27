from django.conf import settings
import http.client
import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
from food_app.views import landing_page
from user_app.models import User
from django.http import HttpResponse



def send_otp_via_email(email):
    subject = "Your account verification email"
    otp = str(random.randint(100000,999999))
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message , email_from , [email])
    return otp

def validateOtp(request):
    user_list=request.session["user_list"]
    print(user_list)
    first_name = user_list[0]
    last_name = user_list[1]
    email = user_list[2]
    phone = user_list[3]
    password = user_list[4]
    generatedotp = user_list[5]
    if request.method != "POST":  
        return render(request, 'authentication_app/otp.html')

    else:
        userotp = request.POST['otp']
        if generatedotp == userotp:
            user = User.objects.create(first_name=first_name,
                                       last_name=last_name,
                                       email=email,
                                       phone=phone,
                                       password=password)
            return redirect(landing_page)
        else:
            return HttpResponse("your otp is wrong")
    
        

    


