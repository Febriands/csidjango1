import json

import requests
import time
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from process.models import CertificationsSteps, CertificationsDetails, StepsForms, CertificationsOfflineDocuments, OfflineDocuments

def index(request, steps_id):
    form_details = []
    document_list = []

    if steps_id:
        steps = CertificationsSteps.objects.filter(id=steps_id).first()

        details = CertificationsDetails.objects.filter(certifications_steps=steps)

        for item in details:
            form_details.append({
                "field": item.steps_forms_id,
                "type": item.steps_forms.form_type,
                "name": item.steps_forms.name,
                "value": item.value
            })

        docs = CertificationsOfflineDocuments.objects.filter(certifications_steps=steps)

        for item in docs:
            if item.files_path:
                path = item.files_path
            else:
                path = None

            document_list.append({
                "field": item.offline_documents_id,
                "name": item.offline_documents.name,
                "path": path
            })
    
    return JsonResponse({
        'done': True,
        'result': {
            "details": form_details,
            "docs": document_list,
        }
    })


def save(request):
    done = False
    message = "Failed"

    steps_id = request.POST.get('steps_id') if request.POST.get('steps_id') else None

    if steps_id:
        steps = CertificationsSteps.objects.filter(id=steps_id).first()

        if steps:
            forms = StepsForms.objects.filter(steps=steps.steps)

            for item in forms:
                value = request.POST.get(str(item.id)) if request.POST.get(str(item.id)) else None

                if value:
                    details = CertificationsDetails.objects.filter(certifications_steps=steps, steps_forms=item).first()

                    if details:
                        details.value = value
                        details.save()

                        steps.certifications.updated = time.time()
                        steps.certifications.save()

                        done = True
                        message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def save_docs(request):
    done = False
    message = "Failed"

    steps_id = request.POST.get('steps_id') if request.POST.get('steps_id') else None

    if steps_id:
        steps = CertificationsSteps.objects.filter(id=steps_id).first()

        if steps:
            docs = OfflineDocuments.objects.filter(steps=steps.steps)

            for item in docs:
                files = request.FILES.getlist(str(item.id)) if request.FILES.getlist(str(item.id)) else None
                
                if files:
                    documents = CertificationsOfflineDocuments.objects.filter(certifications_steps=steps, offline_documents=item).first()
                    
                    if documents:
                        doc = files[0]
                        filename = item.name + " c-" + str(steps.certifications_id) + " " + str(int(time.time())) + "." + doc.name.split('.')[-1]
                        default_storage.save(settings.MEDIA_ROOT + "/docs/" + filename, ContentFile(doc.read()))

                        documents.files_path = filename
                        documents.save()

                        steps.certifications.updated = time.time()
                        steps.certifications.save()

                        done = True
                        message = "Success"

    return JsonResponse({
        'done': done,
        'message': message
    })