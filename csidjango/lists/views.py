from django.views.generic import ListView
from accounts.models import User

# Create your views here.
class UserListView(ListView):
	template_name = "lists/user.html"
	queryset = User.objects.all().order_by('id')
	context_object_name = 'users'

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