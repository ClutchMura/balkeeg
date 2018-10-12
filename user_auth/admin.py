from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import UserContact

# Register your models here.
# admin.site.register(CustomUser, UserAdmin)
admin.site.register(CustomUser)
admin.site.register(UserContact)
