from . import views as auth_views
from django.urls import path

urlpatterns = [
    path('otp/', auth_views.validateOtp, name='otp'),
    path('resend_otp/',auth_views.resend_otp,name='resend_otp')
    
]