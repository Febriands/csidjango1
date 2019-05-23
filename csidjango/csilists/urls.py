from django.urls import path
from . import views

app_name = 'csilists'

urlpatterns = [
    path('user-list/', views.UserListView.as_view(), name = 'userlist'),
]