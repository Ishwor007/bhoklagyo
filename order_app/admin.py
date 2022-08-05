from urllib.request import CacheFTPHandler
from django.contrib import admin

from .models import Order, Cart

admin.site.register(Order)
admin.site.register(Cart)


