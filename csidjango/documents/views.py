from django.shortcuts import render
from . import models

# Create your views here.
def document_manual(request):
    manuals = models.Manual.objects.all()
    return render(request, "documents/manual.html", {'manuals': manuals})

def document_prosedur(request):
    procedures = models.Procedure.objects.all()
    return render(request, "documents/prosedur.html", {'procedures': procedures})

def document_form(request):
    forms = models.Form.objects.all()
    return render(request, "documents/form.html", {'forms': forms})
