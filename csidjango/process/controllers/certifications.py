import json

import requests
import time
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Steps, StepsForms, OfflineDocuments, Certifications, CertificationsSteps, CertificationsDetails, CertificationsOfflineDocuments
from accounts.models import User

def index(request):
    certifications = Certifications.objects.all()
    data = []

    for item in certifications:
        progress_text = str(item.completed) + "/" + str(item.left)
        progress = round(item.completed / item.left, 2)

        data.append({
            "id": item.id,
            "type": item.types.name,
            "name": item.name,
            "applicant": item.applicant.first_name + " " + item.applicant.last_name,
            "progress": progress,
            "progress_text": progress_text,
            "created": item.created,
            "updated": item.updated,
        })
        
    return JsonResponse({
        'done': True,
        'result': data
    })


def get_by_type(request, types_id):
    certifications = Certifications.objects.filter(types_id=types_id)
    certifications = serializers.serialize('json', certifications)
    return JsonResponse({
        'done': True,
        'result': certifications
    })


def save(request):
    done = False
    message = "Failed"

    types_id = request.POST.get('types_id') if request.POST.get('types_id') else None

    if types_id:
        steps = Steps.objects.filter(types_id=types_id).order_by('-order')

        certifications = Certifications()
        certifications.types_id = request.POST.get('types_id')
        certifications.name = request.POST.get('name')
        certifications.applicant = User.objects.filter(id=1).first()
        certifications.completed = 0
        certifications.left = steps.count()
        certifications.created = time.time()
        certifications.updated = time.time()
        certifications.save()

        for step in steps:
            c_steps = CertificationsSteps()
            c_steps.certifications = certifications
            c_steps.steps = step
            c_steps.save()
        
            forms = StepsForms.objects.filter(steps=step)

            for form in forms:
                c_details = CertificationsDetails()
                c_details.certifications_steps = c_steps
                c_details.steps_forms = form
                c_details.save()
                

            documents = OfflineDocuments.objects.filter(steps=step)

            for document in documents:
                c_document = CertificationsOfflineDocuments()
                c_document.certifications_steps = c_steps
                c_document.offline_documents = document
                c_document.save()
            
        done = True
        message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def delete(request):
    done = False
    message = "Failed"

    cert_id = request.GET.get('id')

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