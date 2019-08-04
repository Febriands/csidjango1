from django.urls import path, include
from . import views

from rest_framework import routers

app_name = 'documents'

router = routers.DefaultRouter()
router.register(r'standards', views.StandardViewSet)
router.register(r'manuals', views.ManualViewSet)
router.register(r'procedures', views.ProcedureViewSet)
router.register(r'forms', views.FormViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [    
    path('standar/', views.document_standar, name = 'standar'),
    path('manual/', views.document_manual, name = 'manual'),
    path('prosedur/', views.document_prosedur, name = 'prosedur'),
    path('form/', views.document_form, name = 'form'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]