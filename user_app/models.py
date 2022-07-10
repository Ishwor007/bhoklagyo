from django.db import models
from django.contrib.auth.models import AbstractUser

# user relation
class User(AbstractUser):
    RESTAURANT_ADMIN =1 
    CUSTOMER =2 

    ROLE_CHOICES = (
        (RESTAURANT_ADMIN,'Admin'),
        (CUSTOMER, 'Customer'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=CUSTOMER)

class Customer(User):
    phone = models.CharField(max_length=14, unique=True)

    is_superuser = False 
    is_staff = False
    is_active = True 

    USERNAME_FIELD: str ='phone' 
    class Meta:
        db_table = 'Customer'
    def __str__(self):
        return self.first_name