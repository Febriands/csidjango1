from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [    
    path('manual/', views.document_manual, name = 'manual'),
    path('prosedur/', views.document_prosedur, name = 'prosedur'),
    path('form/', views.document_form, name = 'form'),
]
