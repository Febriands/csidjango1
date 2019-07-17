from django.urls import path
from . import views

app_name = 'process'

urlpatterns = [
    path('types/', views.TypesView.as_view(), name = 'types'),
    path('steps/<int:types_id>/', views.steps, name = 'steps'),
    path('sections/<int:steps_id>/', views.sections, name = 'sections'),
    path('forms/<int:sections_id>/', views.steps_forms, name = 'steps_forms'),
    path('certifications/', views.certifications, name = 'certifications'),
    path('details/<int:cert_id>/', views.details, name = 'details'),
]
