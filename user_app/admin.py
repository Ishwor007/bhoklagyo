from django.contrib import admin

from user_app.models import Customer, User
from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     ordering = ('email','phone')
#     list_display =('email','phone','role',)
#     list_filter = ('RestaurantAdmin__is_staff','RestaurantAdmin__is_admin','RestaurantAdmin__is_active')

# class CustomerAdmin(UserAdmin):
#     ordering = ('phone',)
#     list_display = ('phone','role',)
#     list_filter = ('Customer__is_staff','Customer__is_admin','Customer__is_active')
    
# admin.site.register(User, CustomUserAdmin)
# admin.site.register(Customer, CustomerAdmin)


admin.site.register(User)
admin.site.register(Customer)