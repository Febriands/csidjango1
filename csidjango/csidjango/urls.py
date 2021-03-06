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
from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from lists.controllers import user_list
from process.controllers import certifications, certifications_steps, forms
from process.controllers import offline_documents as docs
from process.controllers import sections, steps, types
from accounts.controllers import sso_controller

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.IndexView.as_view(), name = 'index'),
    path('', views.redirect_view),
    path('dashboard/', views.DashboardView.as_view(), name = 'dashboard'),
    path('error404/', views.Error404View.as_view(), name = 'error404'),
    path('accounts/', include('accounts.urls', namespace = 'accounts')),
    path('users/', include('django.contrib.auth.urls')),
    path('process/', include('process.urls', namespace = 'process')),
    path('reports/', include('reports.urls', namespace = 'reports')),
    path('documents/', include('documents.urls', namespace = 'documents')),

    # api user_list
    path('api/user_list/', user_list.index),
    path('api/user_list/save', user_list.save),
    path('api/user_list/delete', user_list.delete),

    # api types
    path('api/types/', types.index),
    path('api/types/save', types.save),
    path('api/types/delete', types.delete),
    path('api/types/duplicate', types.duplicate),

    # api steps
    path('api/steps/<int:types_id>/', steps.index),
    path('api/steps/save', steps.save),
    path('api/steps/delete', steps.delete),

    # api steps sections
    path('api/sections/<int:steps_id>/', sections.index),
    path('api/sections/save', sections.save),
    path('api/sections/delete', sections.delete),

    # api steps forms
    path('api/forms/<int:sections_id>/', forms.index),
    path('api/forms/save', forms.save),
    path('api/forms/delete', forms.delete),

    # api offline documents forms
    path('api/docs/<int:sections_id>/', docs.index),
    path('api/docs/save', docs.save),
    path('api/docs/delete', docs.delete),

    # api certifications forms
    path('api/certifications/', certifications.index),
    path('api/certifications/<int:types_id>/', certifications.get_by_type),
    path('api/certifications/save', certifications.save),
    path('api/certifications/delete', certifications.delete),

    # api certifications details forms
    path('api/details/<int:steps_id>/', certifications_steps.index),
    path('api/details/save', certifications_steps.save),
    path('api/details/docs/save', certifications_steps.save_docs),
    path('api/details/form/reset/<int:steps_id>/<int:steps_forms_id>/', certifications_steps.reset_form),
    path('api/details/doc/reset/<int:steps_id>/<int:offline_documents_id>/', certifications_steps.reset_doc),

    path('progress/', include('progress.urls', namespace = 'progress')),
    path('schedules/', include('schedules.urls', namespace = 'schedules')),
    path('lists/', include('lists.urls', namespace = 'lists')),

    # sso endpoints
    path('login/callback', sso_controller.authenticate),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
