import json

import requests
import time
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from process.models import Steps, StepsSections, StepsForms, OfflineDocuments, Certifications, CertificationsSteps, CertificationsDetails, CertificationsOfflineDocuments
from accounts.models import User, SSOApplications, Account

def index(request):
    role = request.user.account.current_role

    if role == 0:
        certifications = Certifications.objects.all()
    elif role == 1:
        certifications = Certifications.objects.filter(applicant=request.user)
    else:
        certifications = Certifications.objects.all()
    data = []

    for item in certifications:
        total = CertificationsSteps.objects.filter(certifications=item).count()
        complete = item.completed

        progress_text = str(complete) + "/" + str(total)
        if total > 0:
            progress = round(complete / total * 100)
        else:
            progress = 0

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


@csrf_exempt
def save(request):
    done = False
    message = "Failed"
    user = request.user

    types_id = request.POST.get('types_id') if request.POST.get('types_id') else None

    appkey = request.POST.get('appkey')
    app = SSOApplications.objects.filter(key=appkey).first()

    if app:
        user = save_external_user(app, request.POST.get('customerId'))

    if types_id:
        steps = Steps.objects.filter(types_id=types_id).order_by('-order')

        certifications = Certifications()
        certifications.types_id = request.POST.get('types_id')
        certifications.name = request.POST.get('name')
        certifications.applicant = user
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

            sections = StepsSections.objects.filter(steps=step)

            for section in sections:
                forms = StepsForms.objects.filter(section=section)

                for form in forms:
                    c_details = CertificationsDetails()
                    c_details.certifications_steps = c_steps
                    c_details.steps_forms = form
                    c_details.steps_sections = section
                    c_details.save()

                documents = OfflineDocuments.objects.filter(section=section)

                for document in documents:
                    c_document = CertificationsOfflineDocuments()
                    c_document.certifications_steps = c_steps
                    c_document.offline_documents = document
                    c_document.steps_sections = section
                    c_document.save()
            
        done = True
        message = "Success"
    
    return JsonResponse({
        'done': done,
        'message': message,
        'certification_id': certifications.id
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


def save_external_user(app, user_id):
    if user_id:
        user = User.objects.filter(username=app.name+'-'+user_id).first()

        if not user:
            first_name = ""

            if app.name == "b4t_klik":
                response = requests.post(
                    app.url + "Auth/Login/getProfile",
                    json.dumps(
                        {
                            "customerId": user_id
                        }
                    )
                )
                if response.status_code == 200:
                    customer_data = json.loads(response.content)
                    first_name = customer_data['result']['fullname']

            user = User(username=app.name+'-'+user_id)
            user.set_password('')
            user.first_name = first_name
            user.save()

            account = Account()
            account.user = user
            account.name = first_name
            account.role = "1"
            account.current_role = 1
            account.save()

        return user
    else:
        return False