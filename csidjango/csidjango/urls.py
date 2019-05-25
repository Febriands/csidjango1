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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
