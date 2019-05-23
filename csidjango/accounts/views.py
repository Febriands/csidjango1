from django.shortcuts import render
from django.views.generic import TemplateView,ListView

from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from pprint import pprint
# Create your views here.
class LoginView(TemplateView):
    template_name = "accounts/login.html"

class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

class UserTablesView(ListView):
	template_name = "accounts/user_tables.html"
	queryset = User.objects.all().order_by('id')
	context_object_name = 'users'