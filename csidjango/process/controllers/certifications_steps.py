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

from process.models import CertificationsSteps, CertificationsDetails, StepsForms, StepsSections, CertificationsOfflineDocuments, OfflineDocuments

def index(request, steps_id):
    form_details = []
    document_list = []
    sections_list = {}

    if steps_id:
        steps = CertificationsSteps.objects.filter(id=steps_id).first()
        details = CertificationsDetails.objects.filter(certifications_steps=steps)

        for item in details:
            form_details.append({
                "section": item.steps_sections_id,
                "field": item.steps_forms_id,
                "type": item.steps_forms.form_type,
                "name": item.steps_forms.name,
                "value": item.value,
                "tooltip": item.steps_forms.tooltip,
                "options": item.steps_forms.options,
            })

            sections_list[item.steps_sections_id] = {
                "title": item.steps_sections.title,
                "description": item.steps_sections.description
            }

        docs = CertificationsOfflineDocuments.objects.filter(certifications_steps=steps)

        for item in docs:
            if item.files_path:
                path = item.files_path
            else:
                path = None

            document_list.append({
                "section": item.steps_sections_id,
                "field": item.offline_documents_id,
                "name": item.offline_documents.name,
                "path": path,
                "tooltip": item.offline_documents.tooltip
            })
    
    return JsonResponse({
        'done': True,
        'result': {
            "details": form_details,
            "docs": document_list,
            "sections": sections_list,
        }
    })


def save(request):
    done = False
    message = "Failed"

    steps_id = request.POST.get('steps_id') if request.POST.get('steps_id') else None

    if steps_id:
        steps = CertificationsSteps.objects.filter(id=steps_id).first()

        if steps:
            sections = StepsSections.objects.filter(steps=steps.steps)

            for section in sections:
                forms = StepsForms.objects.filter(section=section)

                for item in forms:
                    if item.form_type == 4:
                        value = ",".join(request.POST.getlist(str(item.id))) if request.POST.getlist(str(item.id)) else None
                    else:
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

            total_forms = CertificationsDetails.objects.filter(certifications_steps=steps).count()
            complete_forms = CertificationsDetails.objects.filter(certifications_steps=steps, value__isnull=False).count()

            if complete_forms == total_forms and not steps.validated:
                steps.validated = True
                steps.save()

                steps.certifications.completed += 1
                steps.certifications.save()

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
            sections = StepsSections.objects.filter(steps=steps.steps)

            for section in sections:
                docs = OfflineDocuments.objects.filter(section=section)

                for item in docs:
                    files = request.FILES.getlist(str(item.id)) if request.FILES.getlist(str(item.id)) else None

                    if files:
                        documents = CertificationsOfflineDocuments.objects.filter(certifications_steps=steps, offline_documents=item).first()

                        if documents:
                            file_list = []
                            i = 1
                            for doc in files:
                                filename = item.name + " " + str(i) + " (doc-" + str(steps.certifications_id) + "-" + str(int(time.time())) + ")." + doc.name.split('.')[-1]
                                default_storage.save(settings.MEDIA_ROOT + "/docs/" + filename, ContentFile(doc.read()))
                                file_list.append(filename)
                                i += 1

                            # Delete old file
                            if documents.files_path:
                                old_file_list = documents.files_path.split("|")
                                for file in old_file_list:
                                    default_storage.delete(settings.MEDIA_ROOT + "/docs/" + file)

                            documents.files_path = "|".join(file_list)
                            documents.save()

                            steps.certifications.updated = time.time()
                            steps.certifications.save()

                            done = True
                            message = "Success"

    return JsonResponse({
        'done': done,
        'message': message
    })


def reset_form(request, steps_id, steps_forms_id):
    done = False
    message = "Failed"

    details = CertificationsDetails.objects.filter(certifications_steps_id=steps_id, steps_forms_id=steps_forms_id).first()

    if details:
        details.value = ""
        details.save()

        details.certifications_steps.validated = False
        details.certifications_steps.save()
        details.certifications_steps.certifications.completed -= 1
        details.certifications_steps.certifications.save()

        done = True
        message = "Success"

    return JsonResponse({
        'done': done,
        'message': message
    })


def reset_doc(request, steps_id, offline_documents_id):
    done = False
    message = "Failed"

    documents = CertificationsOfflineDocuments.objects.filter(certifications_steps_id=steps_id, offline_documents_id=offline_documents_id).first()

    if documents:
        # Delete old file
        if documents.files_path:
            old_file_list = documents.files_path.split("|")
            for file in old_file_list:
                default_storage.delete(settings.MEDIA_ROOT + "/docs/" + file)

        documents.files_path = ""
        documents.save()

        done = True
        message = "Success"

    return JsonResponse({
        'done': done,
        'message': message
    })
