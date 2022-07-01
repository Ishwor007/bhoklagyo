from django.db import models
from user_app.models import User

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.restaurant_name

    
class RestaurantAdmin(models.Model):
    restaurant_name = models.OneToOneField(Restaurant,on_delete=models.CASCADE,related_name='restaurant')
    phone = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=200, unique=True)

    is_superuser = False
    is_staff = True 
    is_active = True

    USERNAME_FIELD: str = 'email'

    class Meta:
        verbose_name = 'Admin'
        permissions = (
            
        )

    def __str__(self):
        return f"{self.restaurant_name}-{self.email}"







