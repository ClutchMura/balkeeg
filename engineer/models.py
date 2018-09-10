from django.db import models
from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     # username = models.ForeignKey(UserProfil, on_delete=models.CASCADE)
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     # first_name=models.CharField(max_length=20)
#     # last_name=models.CharField(max_length=20)
#     first_name=User.first_name
#     last_name=User.last_name
