import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Steps, StepsForms

def index(request, steps_id):
    forms_id = request.GET.get('id') if request.GET.get('id') else None
    
    if forms_id:
        forms = StepsForms.objects.filter(id=forms_id, steps_id=steps_id)
    else:
        forms = StepsForms.objects.filter(steps_id=steps_id)
    
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

    forms.steps_id = request.POST.get('steps_id')
    forms.form_type = request.POST.get('form_type')
    forms.name = request.POST.get('name')
    if forms.save():
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