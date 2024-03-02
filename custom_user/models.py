from django_use_email_as_username.models import BaseUser, BaseUserManager

from django.db import models


class User(BaseUser):
    userID = models.AutoField(primary_key=True, default=None)
    membership_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    objects = BaseUserManager()

