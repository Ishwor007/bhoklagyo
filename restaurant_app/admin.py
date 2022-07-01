from django.contrib import admin

from .models import Restaurant, RestaurantAdmin

admin.site.register(Restaurant)
admin.site.register(RestaurantAdmin)
