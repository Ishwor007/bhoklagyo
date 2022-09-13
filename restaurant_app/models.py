from django.db import models
from user_app.models import User

from user_app.managers import UserManager

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    location        = models.CharField(max_length=200, null=True)
    phone           = models.CharField(max_length=10, unique=True)
    longitude       = models.FloatField(null=True)
    latitude        = models.FloatField(null=True)
    register_date   = models.DateField(auto_now_add=True)
    last_modified_on= models.DateField(auto_now=True)
    is_verified     = models.BooleanField(default=False)

    def __str__(self):
        return self.restaurant_name

    
class RestaurantAdmin(models.Model):
    restaurant = models.OneToOneField(Restaurant,on_delete=models.CASCADE, related_name='restaurant')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
    email = models.EmailField(max_length=200, unique=True)
    role    = User.RESTAURANT_ADMIN
    
    objects = UserManager()

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: list   =['password']
    
    class Meta:
        verbose_name = 'Admin'
        db_table     = 'Admin'
        permissions = (
            
        )

    def __str__(self):
        return f"{self.restaurant}-{self.email}"







