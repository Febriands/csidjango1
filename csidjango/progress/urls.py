from django.urls import path
from . import views

app_name = 'progress'

urlpatterns = [
    path('sertifikasi/', views.ProgressSertifikasiView.as_view(), name = 'sertifikasi'),
]
