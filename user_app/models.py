from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager

# user relation
class User(AbstractBaseUser, PermissionsMixin):
    # username = None
    
    RESTAURANT_ADMIN =1 
    CUSTOMER =2 
    PROJECT_ADMIN = 3

    ROLE_CHOICES = (
        (RESTAURANT_ADMIN,'Restaurant Manager'),
        (CUSTOMER, 'Customer'),
        (PROJECT_ADMIN,'Project Admin')
    )

    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=14, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, default=CUSTOMER)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD: str ='email'
    REQUIRED_FIELDS: list =['password','phone']
    
    
class Customer(User):
    # is_superuser = models.BooleanField(default=False) 
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True) 
    

    USERNAME_FIELD: str ='phone' 
    class Meta:
        db_table = 'Customer'
        verbose_name = 'Customer'
        

    def __str__(self):
        return self.first_name

