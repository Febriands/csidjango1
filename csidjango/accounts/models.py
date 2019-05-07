from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Course(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)