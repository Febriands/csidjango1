from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.LoginView.as_view(), name = 'login'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('user-tables/', views.UserTablesView.as_view(), name = 'user_tables'),
]