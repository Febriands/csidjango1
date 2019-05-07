from django.db import models

# Create your models here.

class Types(models.Model):
    name = models.CharField(max_length=150)


class Steps(models.Model):
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)


class Steps_Forms(models.Model):
    steps = models.ForeignKey(Steps, on_delete=models.CASCADE)
    form_type = models.CharField(max_length=20)
    name = models.CharField(max_length=150)


class Certifications(models.Model):
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    completed = models.IntegerField()
    left = models.IntegerField()
    created = models.BigIntegerField()
    updated = models.BigIntegerField()

class Certifications_Details(models.Model):
    certifications = models.ForeignKey(Certifications, on_delete=models.CASCADE)
    steps = models.ForeignKey(Steps, on_delete=models.CASCADE)
    steps_forms = models.ForeignKey(Steps_Forms, on_delete=models.CASCADE)
    value = models.TextField()
