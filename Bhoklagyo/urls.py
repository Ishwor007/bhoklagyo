
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from food_app import views as food_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', food_views.landing_page, name ='landing_page'),

    path('food_app/',include('food_app.urls')),
    path('user_app/',include('user_app.urls')),
    path('authentication_app/', include('authentication_app.urls')),
    path('restaurant_app/', include('restaurant_app.urls')),
    path('order_app/', include('order_app.urls')),

    path('khalti/', include('khalti.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)