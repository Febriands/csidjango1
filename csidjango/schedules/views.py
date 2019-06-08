from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class SchedulesUmumView(TemplateView):
    template_name = "schedules/umum.html"
