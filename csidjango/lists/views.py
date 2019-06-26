from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from accounts.models import User

# Create your views here.

# class UserListView(TemplateView):
# 	template_name = "lists/user.html"
	# queryset = User.objects.all().order_by('id')
	# context_object_name = 'users'

def user_list(request):
    return render(request, "lists/user.html")

class OrganisasiListView(ListView):
	template_name = "lists/organisasi.html"
	queryset = User.objects.all().order_by('id')
	context_object_name = 'users'

class AuditorListView(ListView):
	template_name = "lists/auditor.html"
	queryset = User.objects.all().order_by('id')
	context_object_name = 'users'

class SertifikatListView(ListView):
	template_name = "lists/sertifikat.html"
	queryset = User.objects.all().order_by('id')
	context_object_name = 'users'