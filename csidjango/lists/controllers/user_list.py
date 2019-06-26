import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from accounts.models import Account

def index(request):
    user_id = request.GET.get('id') if request.GET.get('id') else None
   
    if user_id:
        user = Account.objects.filter(id=user_id)
    else:
        user = Account.objects.all()

    user = serializers.serialize('json', user)

    return JsonResponse({
        'done': True,
        'result': user
    })


def save(request):
    done = False
    message = "Failed"

    user_id = request.POST.get('id') if request.POST.get('id') != "" else None
   
    if user_id:
        user = Account.objects.get(id=user_id)
    else:
        user = Account()

    user.name = request.POST.get('name')
    if user.save():
        done = True
        message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })


def delete(request):
    done = False
    message = "Failed"

    user_id = request.GET.get('id') if request.GET.get('id') else None

    if user_id:
        user = Account.objects.filter(id=user_id).first()
        if user:
            user.delete()
            
            done = True
            message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message
    })