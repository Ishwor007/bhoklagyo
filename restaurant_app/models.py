from django.db import models
from user_app.models import User

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, unique=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    register_date = models.DateField(auto_now_add=True)
    last_modified_on = models.DateField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.restaurant_name

    
class RestaurantAdmin(User):
    restaurant_name = models.OneToOneField(Restaurant,on_delete=models.CASCADE,related_name='restaurant')
    
    role = User.RESTAURANT_ADMIN
    
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







