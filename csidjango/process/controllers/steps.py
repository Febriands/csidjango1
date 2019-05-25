import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Types, Steps

def index(request, types_id):
    steps = Steps.objects.filter(types_id=types_id)
    steps = serializers.serialize('json', steps)
    return JsonResponse({
        'done': True,
        'result': steps
    })


def save(request):
    done = False
    message = "Failed"

    steps_id = request.POST.get('id')

    if steps_id:
        steps = Steps.objects.get(id=steps_id)
    else:
        steps = Steps()

    steps.types_id = request.POST.get('types_id')
    steps.name = request.POST.get('name')
    if steps.save():
        done = True
        message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def delete(request):
    done = False
    message = "Failed"

    steps_id = request.POST.get('id')

    if steps_id:
        steps = Steps.objects.filter(id=steps_id).first()
        if steps:
            steps.delete()
            
            done = True
            message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })