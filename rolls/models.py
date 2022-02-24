from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)