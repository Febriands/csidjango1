import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Steps, StepsForms, Certifications

def index(request, types_id):
    certifications = Certifications.objects.filter(types_id=types_id)
    certifications = serializers.serialize('json', certifications)
    return JsonResponse({
        'done': True,
        'result': certifications
    })


def save(request):
    done = False
    message = "Failed"

    cert_id = request.POST.get('id')

    if cert_id:
        certifications = Certifications.objects.get(id=cert_id)
        certifications.completed = request.POST.get('completed')

        certifications.updated = time.time()
    else:
        certifications = Certifications()
        certifications.types_id = request.POST.get('types_id')
        certifications.completed = 0
        certifications.left = Steps.objects.filter(types_id=request.POST.get('types_id')).count()
        certifications.created = time.time()
        certifications.updated = time.time()

    if certifications.save():
        done = True
        message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def delete(request):
    done = False
    message = "Failed"

    cert_id = request.POST.get('id')

    if cert_id:
        certifications = Certifications.objects.filter(id=cert_id).first()
        if certifications:
            certifications.delete()
            
            done = True
            message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })