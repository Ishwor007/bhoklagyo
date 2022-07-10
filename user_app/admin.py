from django.contrib import admin

from user_app.models import Customer, User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    ordering = ('email','phone',)
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Customer)
