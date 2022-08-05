from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Restaurant, RestaurantAdmin

class CustomRestaurantAdmin(UserAdmin):
    ordering = ('email',)
    list_display =('email','phone','role','is_superuser','is_staff','is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','phone', 'password'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','phone')
    filter_horizontal = ()

admin.site.register(Restaurant)
admin.site.register(RestaurantAdmin, CustomRestaurantAdmin)
