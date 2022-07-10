from django.db import models

from django.contrib.auth.models import AbstractUser

# user relation
class User(AbstractUser):
    username = None
    
    RESTAURANT_ADMIN =1 
    CUSTOMER =2 

    ROLE_CHOICES = (
        (RESTAURANT_ADMIN,'Admin'),
        (CUSTOMER, 'Customer'),
    )

    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=14, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, default=CUSTOMER)
    USERNAME_FIELD: str ='email'
    REQUIRED_FIELDS: list =['password','phone']

    

class Customer(User):
    is_superuser = False 
    is_staff = False
    is_active = True 


    USERNAME_FIELD: str ='phone'

    class Meta:
        verbose_name = 'Customer'
        

    def __str__(self):
        return self.first_name

