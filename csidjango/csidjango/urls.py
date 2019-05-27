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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name = 'index'),
    path('dashboard/', views.DashboardView.as_view(), name = 'dashboard'),
    path('error404', views.Error404View.as_view(), name = 'error404'),
    path('accounts/', include('accounts.urls', namespace = 'accounts')),
    path('process/', include('process.urls', namespace = 'process')),
    path('progress/', include('progress.urls', namespace = 'progress')),
    path('schedules/', include('schedules.urls', namespace = 'schedules')),
    path('lists/', include('lists.urls', namespace = 'lists')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
