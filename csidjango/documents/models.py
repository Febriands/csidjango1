from django.db import models

# Create your models here.
class Manual(models.Model):
    name = models.CharField(max_length=150)
    code =  models.EmailField(max_length=150)
    version = models.IntegerField(default=0)  
    active = models.BooleanField(default=False)
    date_actived = models.BigIntegerField()
    date_deactived = models.BigIntegerField()
       
    def __str__(self):
        return self.name

class Procedure(models.Model):
    name = models.CharField(max_length=150)
    code =  models.EmailField(max_length=150)
    version = models.IntegerField(default=0)  
    active = models.BooleanField(default=False)
    date_actived = models.BigIntegerField()
    date_deactived = models.BigIntegerField()
       
    def __str__(self):
        return self.name

class Form(models.Model):
    name = models.CharField(max_length=150)
    code =  models.EmailField(max_length=150)
    version = models.IntegerField(default=0)  
    active = models.BooleanField(default=False)
    date_actived = models.BigIntegerField()
    date_deactived = models.BigIntegerField()
       
    def __str__(self):
        return self.name