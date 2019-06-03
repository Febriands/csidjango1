from django.shortcuts import render
from django.views.generic import TemplateView

from process.models import Types, Steps

# Create your views here.

class HomeView(TemplateView):
    template_name = "process/home.html"

class TablesView(TemplateView):
    template_name = "process/tables.html"

class TypesView(TemplateView):
    template_name = "process/types.html"

def steps(request, types_id):
    types = Types.objects.filter(id=types_id).first()

    return render(request, "process/steps.html", {
        "types_id": types.id,
        "types_name": types.name,
    })

def steps_forms(request, steps_id):
    steps = Steps.objects.filter(id=steps_id).first()

    return render(request, "process/steps_forms.html", {
        "steps_id": steps.id,
        "steps_name": steps.name,
    })

def certifications(request):
    return render(request, "process/certifications.html")