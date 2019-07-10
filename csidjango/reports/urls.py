from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [    
    path('sertifikasi/', views.report_sertifikasi, name = 'sertifikasi'),
]
