from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Manual)
admin.site.register(models.Procedure)
admin.site.register(models.Form)