from django.db import models
from django.utils.text import slugify

# Create your models here.
class Standar(models.Model):
    name = models.CharField(max_length=150)
    code =  models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now=True)
    standar_doc = models.FileField(upload_to='standar/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug != slugify('%s %s' % (self.name, self.version)):
        # Newly created object, so set slug
            self.slug = slugify('%s %s' % (self.name, self.version))
        super(Form, self).save(*args, **kwargs)    
       
    def __str__(self):
        return self.name


class Manual(models.Model):
    standar = models.ForeignKey(Standar, related_name='manual_standar', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    code =  models.CharField(max_length=150)
    version = models.IntegerField(default=0,)  
    date_created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    date_actived = models.DateTimeField(null=True, blank=True)
    date_deactived = models.DateTimeField(null=True, blank=True)
    manual_doc = models.FileField(upload_to='manual/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug != slugify('%s %s' % (self.name, self.version)):
        # Newly created object, so set slug
            self.slug = slugify('%s %s' % (self.name, self.version))
        super(Manual, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Procedure(models.Model):
    manual = models.ForeignKey(Manual, related_name='manual_procedure', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    code =  models.CharField(max_length=150)
    version = models.IntegerField(default=0)  
    date_created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    date_actived = models.DateTimeField(null=True, blank=True)
    date_deactived = models.DateTimeField(null=True, blank=True)
    procedure_doc = models.FileField(upload_to='prosedur/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug != slugify('%s %s' % (self.name, self.version)):
        # Newly created object, so set slug
            self.slug = slugify('%s %s' % (self.name, self.version))
        super(Procedure, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Form(models.Model):
    manual = models.ForeignKey(Manual, related_name='form_manual', on_delete=models.CASCADE, null=True, blank=True)
    procedure = models.ForeignKey(Procedure, related_name='form_procedure', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    code =  models.CharField(max_length=150)
    version = models.IntegerField(default=0)  
    date_created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    date_actived = models.DateTimeField(null=True, blank=True)
    date_deactived = models.DateTimeField(null=True, blank=True)
    form_doc = models.FileField(upload_to='form/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug != slugify('%s %s' % (self.name, self.version)):
        # Newly created object, so set slug
            self.slug = slugify('%s %s' % (self.name, self.version))
        super(Form, self).save(*args, **kwargs)    
       
    def __str__(self):
        return self.name
