from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)