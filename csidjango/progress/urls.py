from django.urls import path
from . import views

app_name = 'progress'

urlpatterns = [
    path('sertifikasi/', views.ProgressSertifikasiView.as_view(), name = 'sertifikasi'),
    path('dokumen/', views.ProgressDokumenView.as_view(), name = 'dokumen'),
    path('audit/', views.ProgressAuditView.as_view(), name = 'audit'),
]
