from . import views as auth_views
from django.urls import path

urlpatterns = [
    path('otp/', auth_views.validateOtp, name='otp'),
    
]