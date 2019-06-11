from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ProgressSertifikasiView(TemplateView):
    template_name = "progress/sertifikasi.html"

class ProgressDokumenView(TemplateView):
    template_name = "progress/dokumen.html"

class ProgressAuditView(TemplateView):
    template_name = "progress/audit.html"