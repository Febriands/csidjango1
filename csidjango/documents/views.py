from django.shortcuts import render
from . import models

from rest_framework import viewsets
from . import serializers

# Create your views here.
def document_standar(request):
    standards = models.Standard.objects.all()
    return render(request, "documents/standar.html", {'standars': standards})

def document_manual(request):
    manuals = models.Manual.objects.all()
    return render(request, "documents/manual.html", {'manuals': manuals})

def document_prosedur(request):
    procedures = models.Procedure.objects.all()
    return render(request, "documents/prosedur.html", {'procedures': procedures})

def document_form(request):
    forms = models.Form.objects.all()
    return render(request, "documents/form.html", {'forms': forms})

class StandardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Standard.objects.all().order_by('id')
    serializer_class = serializers.StandardSerializer

class ManualViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Manual.objects.all().order_by('id')
    serializer_class = serializers.ManualSerializer

class ProcedureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Procedure.objects.all().order_by('id')
    serializer_class = serializers.ProcedureSerializer

class FormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Form.objects.all().order_by('id')
    serializer_class = serializers.FormSerializer