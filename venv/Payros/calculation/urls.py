from django.urls import path

from . import views

urlpatterns = [
    path('', views.calculation_view, name='calculation_view'),
    path('calculation_edit', views.calculation_edit, name='calculation_edit'), 
]