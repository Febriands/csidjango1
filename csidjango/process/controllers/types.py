import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Types, Steps, StepsForms, OfflineDocuments

def index(request):
    types_id = request.GET.get('id') if request.GET.get('id') else None

    if types_id:
        types = Types.objects.filter(id=types_id)
    else:
        types = Types.objects.all()

    types = serializers.serialize('json', types)
    return JsonResponse({
        'done': True,
        'result': types
    })


def save(request):
    done = False
    message = "Failed"

    types_id = request.POST.get('id') if request.POST.get('id') != "" else None

    if types_id:
        types = Types.objects.get(id=types_id)
    else:
        types = Types()

    types.name = request.POST.get('name')
    if types.save():
        done = True
        message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def delete(request):
    done = False
    message = "Failed"

    types_id = request.GET.get('id') if request.GET.get('id') else None

    if types_id:
        types = Types.objects.filter(id=types_id).first()
        if types:
            types.delete()
            
            done = True
            message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def duplicate(request):
    done = False
    message = "Failed"

    source_id = request.POST.get('source_id') if request.POST.get('source_id') != "" else None

    if source_id:
        new_types = Types()
        new_types.name = request.POST.get('name')
        new_types.active = False
        new_types.save()

        steps = Steps.objects.filter(types_id=source_id)

        for step in steps:
            new_steps = Steps()
            new_steps.types = new_types
            new_steps.order = step.order
            new_steps.name = step.name
            new_steps.save()

            forms = StepsForms.objects.filter(steps=step)

            for form in forms:
                new_forms = StepsForms()
                new_forms.steps = new_steps
                new_forms.form_type = form.form_type
                new_forms.name = form.name
                new_forms.save()

            documents = OfflineDocuments.objects.filter(steps=step)

            for document in documents:
                new_documents = OfflineDocuments()
                new_documents.steps = new_steps
                new_documents.name = document.name
                new_documents.save()

        done = True
        message = "Success"

    return JsonResponse({
        'done': done,
        'message': message
    })
