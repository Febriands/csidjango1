import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Steps, StepsForms

def index(request, sections_id):
    forms_id = request.GET.get('id') if request.GET.get('id') else None
    
    if forms_id:
        forms = StepsForms.objects.filter(id=forms_id, section_id=sections_id)
    else:
        forms = StepsForms.objects.filter(section_id=sections_id)
    
    forms = serializers.serialize('json', forms)
    return JsonResponse({
        'done': True,
        'result': forms
    })


def save(request):
    done = False
    message = "Failed"

    forms_id = request.POST.get('id') if request.POST.get('id') else None

    if forms_id:
        forms = StepsForms.objects.get(id=forms_id)
    else:
        forms = StepsForms()

    forms.section_id = request.POST.get('sections_id')
    forms.form_type = request.POST.get('form_type')
    forms.name = request.POST.get('name')
    forms.tooltip = request.POST.get('tooltip')
    forms.options = request.POST.get('options')
    forms.save()

    done = True
    message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def delete(request):
    done = False
    message = "Failed"

    forms_id = request.GET.get('id') if request.GET.get('id') else None

    if forms_id:
        forms = StepsForms.objects.filter(id=forms_id).first()
        if forms:
            forms.delete()
            
            done = True
            message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })