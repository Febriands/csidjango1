from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class LoginView(TemplateView):
    template_name = "accounts/login.html"

class ProfileView(TemplateView):
    template_name = "accounts/profile.html"