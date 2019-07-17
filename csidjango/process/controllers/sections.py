import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Steps, StepsSections, StepsSections


def index(request, steps_id):
    section_id = request.GET.get('id') if request.GET.get('id') else None
    
    if section_id:
        sections = StepsSections.objects.filter(id=section_id, steps_id=steps_id)
    else:
        sections = StepsSections.objects.filter(steps_id=steps_id)
    
    sections = serializers.serialize('json', sections)
    return JsonResponse({
        'done': True,
        'result': sections
    })


def save(request):
    done = False
    message = "Failed"

    section_id = request.POST.get('id') if request.POST.get('id') else None

    if section_id:
        sections = StepsSections.objects.get(id=section_id)
    else:
        sections = StepsSections()

    sections.steps_id = request.POST.get('steps_id')
    sections.title = request.POST.get('title')
    sections.description = request.POST.get('description')
    sections.save()

    done = True
    message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def delete(request):
    done = False
    message = "Failed"

    section_id = request.GET.get('id') if request.GET.get('id') else None

    if section_id:
        sections = StepsSections.objects.filter(id=section_id).first()
        if sections:
            sections.delete()
            
            done = True
            message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })