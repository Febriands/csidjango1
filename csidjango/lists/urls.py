from django.urls import path
from . import views

app_name = 'lists'

urlpatterns = [    
    path('user/', views.UserListView.as_view(), name = 'user'),
    path('organisasi/', views.OrganisasiListView.as_view(), name = 'organisasi'),
    path('auditor/', views.AuditorListView.as_view(), name = 'auditor'),
    path('sertifikat/', views.SertifikatListView.as_view(), name = 'sertifikat'),
]
