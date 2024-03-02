from django.contrib import admin
from django_use_email_as_username.admin import BaseUserAdmin

from .models import User


# admin.site.register(User, BaseUserAdmin)

@admin.register(User)
class AdminBaseUser(admin.ModelAdmin):
    list_display = ['userID', 'membership_date', 'name']
