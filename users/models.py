"""
Model class UserInfo which extends the User model class.

"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, User

from recommend import settings


class Profile(models.Model):
    user = models.ForeignKey(User)
    gender = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    pic_url = models.CharField(max_length=255, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

