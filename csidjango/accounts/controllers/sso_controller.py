import json
import requests

import requests
from django.urls import reverse
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from accounts.models import User, Account, SSOApplications, Roles
from process.models import Certifications

def authenticate(request):
    status = False
    message = "Failed"
    result = []

    appkey = request.GET.get('appkey')

    app = SSOApplications.objects.filter(key=appkey).first()

    if app:
        if app.name == "b4t":
            employee_id = request.GET.get('employee_id')
            role = Roles.objects.filter(name=request.GET.get('role')).first()
            
            if role:
                role_id = str(role.role_id)
                current_role_id = role.role_id
            else:
                role_id = "0"
                current_role_id = 0

            if employee_id:
                user = User.objects.filter(username='b4t-'+employee_id).first()

                if user:
                    current_roles = user.account.role.split(",")
                    
                    if not role_id in current_roles:
                        current_roles.append(role_id)

                    role_id = ",".join(current_roles)
                    user.account.role = role_id
                    user.account.current_role = current_role_id
                    user.account.save()
                else:
                    first_name = None
                    response = requests.get(app.url +'api/v1/employee?nip='+ request.GET.get('nip') +'&appkey='+app.key)
                    
                    if response.status_code == 200:
                        employee_data = json.loads(response.content)
                        first_name = employee_data['name']

                    user = User(username='b4t-'+employee_id)
                    user.set_password('')
                    user.first_name = first_name
                    user.is_staff = True
                    user.save()

                    account = Account()
                    account.user = user
                    account.name = first_name
                    account.role = role_id
                    account.current_role = current_role_id
                    account.save()

                login(request, user)
                return redirect('dashboard')
            else:
                message = "Employee ID not found"
                logout(request)
        elif app.name == "b4t_klik":
            customer_id = request.GET.get('customerId')

            if customer_id:
                user = User.objects.filter(username='b4t_klik-'+customer_id).first()

                if not user:
                    first_name = None
                    response = requests.post(
                        app.url +'Auth/Login/getProfile',
                        json.dumps(
                            {
                                "customerId": request.GET.get('customerId')
                            }
                        )
                    )
                    if response.status_code == 200:
                        customer_data = json.loads(response.content)
                        first_name = customer_data['result']['fullname']

                    user = User(username='b4t_klik-'+customer_id)
                    user.set_password('')
                    user.first_name = first_name
                    user.save()

                    account = Account()
                    account.user = user
                    account.name = first_name
                    account.role = "1"
                    account.current_role = 1
                    account.save()

                login(request, user)

                certification_id = request.GET.get('certification_id')

                if certification_id:
                    certification = Certifications.objects.filter(id=certification_id).first()

                    if certification:
                        if certification.applicant_id == user.id:
                            return HttpResponseRedirect(reverse('process:details', args=[certification.id]))
                        else:
                            message = "Certification not belongs to you"
                            logout(request)
                    else:
                        message = "Certification not found"
                        logout(request)
                else:
                    message = "Certification ID not found"
                    logout(request)
            else:
                message = "Customer ID not found"
    else:
        message = "Application not found"
    return JsonResponse({
        'status': status,
        'message': message,
        'result': result,
    })