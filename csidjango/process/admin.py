from django.contrib import admin
from .models import Types, Steps, Certifications, StepsForms, OfflineDocuments

# Register your models here.
admin.site.register(Types)
admin.site.register(Steps)
admin.site.register(StepsForms)
admin.site.register(OfflineDocuments)
admin.site.register(Certifications)
