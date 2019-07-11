from django.db import models

# Create your models here.
class Manual(models.Model):
    name = models.CharField(max_length=150)
    code =  models.CharField(max_length=150)
    version = models.IntegerField(default=0)  
    date_created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    date_actived = models.DateTimeField(null=True, blank=True)
    date_deactived = models.DateTimeField(null=True, blank=True)
    manual = models.FileField(upload_to='manual/', null=True, blank=True)
       
    def __str__(self):
        return self.name

class Procedure(models.Model):
    name = models.CharField(max_length=150)
    code =  models.CharField(max_length=150)
    version = models.IntegerField(default=0)  
    date_created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    date_actived = models.DateTimeField(null=True, blank=True)
    date_deactived = models.DateTimeField(null=True, blank=True)
    procedure = models.FileField(upload_to='prosedur/', null=True, blank=True)
       
    def __str__(self):
        return self.name

class Form(models.Model):
    name = models.CharField(max_length=150)
    code =  models.CharField(max_length=150)
    version = models.IntegerField(default=0)  
    date_created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    date_actived = models.DateTimeField(null=True, blank=True)
    date_deactived = models.DateTimeField(null=True, blank=True)
    form = models.FileField(upload_to='form/', null=True, blank=True)
       
    def __str__(self):
        return self.name
