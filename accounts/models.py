# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=150)
