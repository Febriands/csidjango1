from django.urls import path
from . import views

app_name = 'process'

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('tables/', views.TablesView.as_view(), name = 'tables'),
    path('types/', views.TypesView.as_view(), name = 'types'),
    path('steps/<int:types_id>/', views.steps, name = 'steps'),
]
