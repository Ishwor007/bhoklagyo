from django.urls import path

from .views import login_admin, register_admin, register_restaurant

urlpatterns = [
    path('register-admin', register_admin),
    path('register-restaurant', register_restaurant),
    path('login-admin', login_admin),
]