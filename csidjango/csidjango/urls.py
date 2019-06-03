"""csidjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

from process.controllers import types
from process.controllers import steps
from process.controllers import forms
from process.controllers import offline_documents as docs
from process.controllers import certifications
from process.controllers import certifications_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name = 'index'),
    path('accounts/', include('accounts.urls', namespace = 'accounts')),
    path('process/', include('process.urls', namespace = 'process')),

    # api types
    path('api/types/', types.index),
    path('api/types/save', types.save),
    path('api/types/delete', types.delete),

    # api steps
    path('api/steps/<int:types_id>/', steps.index),
    path('api/steps/save', steps.save),
    path('api/steps/delete', steps.delete),

    # api steps forms
    path('api/forms/<int:steps_id>/', forms.index),
    path('api/forms/save', forms.save),
    path('api/forms/delete', forms.delete),

    # api offline documents forms
    path('api/docs/<int:steps_id>/', docs.index),
    path('api/docs/save', docs.save),
    path('api/docs/delete', docs.delete),

    # api certifications forms
    path('api/certifications/<int:types_id>/', certifications.index),
    path('api/certifications/save', certifications.save),
    path('api/certifications/delete', certifications.delete),

    # api certifications details forms
    path('api/details/<int:cert_id>/<int:steps_id>/', certifications_details.index),
    path('api/details/save', certifications_details.save),
    path('api/details/delete', certifications_details.delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
