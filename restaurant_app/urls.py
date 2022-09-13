from django.urls import path

from . import views as restaurant_views

urlpatterns = [
    # path('', restaurant_views.show_menu, name = 'show_menu'),
    path('register-admin', restaurant_views.register_admin, name = 'register-restaurant-admin'),
    path('register-restaurant-form', restaurant_views.register_restaurant_form, name='register-restaurant-form'),
    path('register-restaurant', restaurant_views.register_restaurant, name='register-restaurant'),
    path('login-restaurant', restaurant_views.login_admin, name = 'login-restaurant'),
    path('dashboard', restaurant_views.dashboard, name="dashboard" ),
    path('logout-admin', restaurant_views.logout_admin, name = 'logout-admin'),
    # path('update_menu/<str:id>',restaurant_views.update_item, name = 'update-menu'),
]