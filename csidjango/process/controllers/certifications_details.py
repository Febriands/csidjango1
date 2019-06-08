import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import CertificationsDetails, Certifications

def index(request, cert_id, steps_id):
    details = CertificationsDetails.objects.filter(certifications_id=cert_id, steps_id=steps_id)
    details = serializers.serialize('json', details)
    return JsonResponse({
        'done': True,
        'result': details
    })


def save(request):
    done = False
    message = "Failed"

    details_id = request.POST.get('id')

    if details_id:
        details = CertificationsDetails.objects.get(id=details_id)
    else:
        details = CertificationsDetails()

    details.steps_id = request.POST.get('steps_id')
    details.steps_forms_id = request.POST.get('steps_forms_id')
    details.value = request.POST.get('value')

    if details.save():
        done = True
        message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def delete(request):
    done = False
    message = "Failed"

    details_id = request.POST.get('id')

    if details_id:
        details = Certifications.objects.filter(id=details_id).first()
        if details:
            details.delete()
            
            done = True
            message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })