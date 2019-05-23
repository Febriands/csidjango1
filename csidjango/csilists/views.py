from django.shortcuts import render
from django.views.generic import ListView

from accounts.models import User

# Create your views here.
class UserListView(ListView):
	template_name = "csilists/user_list.html"
	queryset = User.objects.all().order_by('id')
	context_object_name = 'users'