import json

import requests
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from accounts.models import Account

def index(request):
    user_id = request.GET.get('id') if request.GET.get('id') else None
    # users = User.objects.all()
    # data = []
    if user_id:
        user = Account.objects.filter(id=user_id)
    else:
        user = Account.objects.all()

    user = serializers.serialize('json', user)
    # for item in users:
    #     data.append({
    #             "id": item.id,
    #             "username": item.username,            
    #         })

    return JsonResponse({
        'done': True,
        'result': user
    })


def save(request):
    done = False
    message = "Failed"

    # user_id = request.POST.get('id') if request.POST.get('id') != "" else None
    user_id = request.POST.get('user_id') if request.POST.get('user_id') else None

    # if user_id:
    #     user = User.objects.get(id=user_id)
    #     user.user_id = request.POST.get('user_id')
    #     user.username = request.POST.get('username')
    #     user.save()

    #     done = True
    #     message = "Success"
    if user_id:
        user = Account.objects.get(id=types_id)
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

    # user_id = request.GET.get('id') if request.GET.get('id') else None
    user_id = request.GET.get('id')

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