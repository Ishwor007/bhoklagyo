from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserManager(BaseUserManager):
    def create_superuser(self, email, phone, password, **extra_fields):
        if email is None:
            raise ValueError("Email is a required field.")
        if not password:
            raise ValueError("Can't create User without a password!")
        
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)
        
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )
        user.is_staff = True
        user.is_superuser = True 
        user.role = settings.AUTH_USER_MODEL.PROJECT_ADMIN
        
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user 
    
    def create_staffuser(self, email, phone, password=None, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        if email is None:
            raise ValueError("Email is a required field.")
        if not password:
            raise ValueError("Can't create User without a password!")
        
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_active', True)
        
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )
        user.is_staff = True
        user.role = settings.AUTH_USER_MODEL.RESTAURANT_ADMIN
  
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user 
    
    def create_user(self, phone, password=None, **extra_fields):
        if phone is None:
            raise ValueError("Phone is a required field.")
        
        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_active', True)
        
        user = self.model(
            phone=phone,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user