from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class UserProfile(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    profile_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    curriculum_vitae = models.FileField(upload_to='curriculum_vitae/', null=True, blank=True)    