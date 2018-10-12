from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import models as auth_models
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.conf import settings

class CustomUser(AbstractBaseUser, auth_models.PermissionsMixin):
    username_validator = ASCIIUsernameValidator()

    """カスタムユーザーモデル."""
    class Meta:
        db_table = 'custom_user'

    username = models.CharField(max_length=10,unique=True)
    # username = models.CharField(max_length=10,unique=True)
    email = models.EmailField(unique=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # Default Permission
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = auth_models.UserManager()

    def __str__(self):
        return self.username

#各ユーザへのコンタクト方法を管理するモデル
class UserContact(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    contact_type=models.CharField(max_length=10)
    contact_link=models.URLField(max_length=200)

    def __str__(self):
        return str(self.username)
