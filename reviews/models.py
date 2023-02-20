# reviews/models.py

from django.db import models

class Review(models.Model):
    author      = models.CharField(max_length=150)
    position    = models.CharField(max_length=150)
    company     = models.CharField(max_length=150)
    review      = models.TextField()
    publish     = models.BooleanField(default=True)