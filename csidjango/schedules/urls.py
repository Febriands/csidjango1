from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [    
    path('umum/', views.SchedulesUmumView.as_view(), name = 'umum'),
]
