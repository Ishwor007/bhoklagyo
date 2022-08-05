from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms


from user_app.models import Customer, Admin

    
class CustomerAdmin(UserAdmin):
    list_display = ('phone','first_name','last_name','is_superuser','is_staff','is_active')

    fieldsets = (
        (None, {'fields': ('phone', 'password', 'first_name', 'last_name')}),

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

    
admin.site.register(Customer, CustomerAdmin)


# admin.site.register(User)
# admin.site.register(Customer)