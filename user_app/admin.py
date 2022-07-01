from django.contrib import admin
from user_app.models import Customer, User
from django.contrib.auth.admin import UserAdmin
    
admin.site.register(User, UserAdmin)
admin.site.register(Customer)




