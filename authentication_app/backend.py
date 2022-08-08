from django.contrib.auth.backends import BaseBackend
from django.db.models import Q

from user_app.models import User


class EmailOrPhoneBackend(BaseBackend):
    def authenticate(self, request, phone=None, password=None):
        try:
            user = User.objects.get(
                phone=phone,
            )
            pwd_valid = user.check_password(password)
            if pwd_valid:            
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None