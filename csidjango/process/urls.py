from django.urls import path
from . import views

app_name = 'process'

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('tables/', views.TablesView.as_view(), name = 'tables'),
]
