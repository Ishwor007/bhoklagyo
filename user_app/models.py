from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

import datetime

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    RESTAURANT_ADMIN    = 1 
    CUSTOMER            = 2
    PROJECT_ADMIN       = 3

    ROLE_CHOICES = (
        (RESTAURANT_ADMIN,'Restaurant Manager'),
        (CUSTOMER, 'Customer'),
        (PROJECT_ADMIN,'Project Admin')
    )

    email           = models.EmailField(max_length=255, unique=True)
    phone           = models.CharField(max_length=14, unique=True)
    role            = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, default=CUSTOMER)
    date_joined     = models.DateTimeField(auto_now_add=True)
    is_staff        = models.BooleanField(default=False) 
    is_superuser    = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD: str     ='email'
    REQUIRED_FIELDS: list   =['password','phone']
    
    
class Customer(User):
    first_name:str  = models.CharField(max_length=255)
    last_name:str   = models.CharField(max_length=255)
    

    USERNAME_FIELD: str ='phone' 
    
    class Meta:
        db_table        = 'Customer'
        verbose_name    = 'Customer'
        

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

