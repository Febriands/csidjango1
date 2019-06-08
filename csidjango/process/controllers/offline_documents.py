import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Steps, OfflineDocuments

def index(request, steps_id):
    doc_id = request.GET.get('id') if request.GET.get('id') else None
    
    if doc_id:
        docs = OfflineDocuments.objects.filter(id=doc_id, steps_id=steps_id)
    else:
        docs = OfflineDocuments.objects.filter(steps_id=steps_id)
    
    docs = serializers.serialize('json', docs)
    return JsonResponse({
        'done': True,
        'result': docs
    })


def save(request):
    done = False
    message = "Failed"

    doc_id = request.POST.get('id') if request.POST.get('id') else None

    if doc_id:
        docs = OfflineDocuments.objects.get(id=doc_id)
    else:
        docs = OfflineDocuments()

    docs.steps_id = request.POST.get('steps_id')
    docs.name = request.POST.get('name')
    if docs.save():
        done = True
        message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def delete(request):
    done = False
    message = "Failed"

    doc_id = request.GET.get('id') if request.GET.get('id') else None

    if doc_id:
        docs = OfflineDocuments.objects.filter(id=doc_id).first()
        if docs:
            docs.delete()
            
            done = True
            message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })