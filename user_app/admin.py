from django.contrib import admin

from user_app.models import Customer, User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    ordering = ('email','phone')
    list_display =('email','phone','role','is_superuser','is_staff','is_active')
    # list_filter = ('RestaurantAdmin__is_staff','RestaurantAdmin__is_admin','RestaurantAdmin__is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password'),
        }),
    )
    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()
    
class CustomerAdmin(UserAdmin):
    ordering = ('phone',)
    list_display = ('phone',)
    # list_filter = ('Customer__is_staff','Customer__is_admin','Customer__is_active')    

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password'),
        }),
    )
    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()

    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Customer, CustomerAdmin)


# admin.site.register(User)
# admin.site.register(Customer)