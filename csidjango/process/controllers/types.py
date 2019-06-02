import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Types

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

    types_id = request.GET.get('id')

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