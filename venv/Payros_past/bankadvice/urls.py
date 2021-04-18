from django.urls import path

from . import views

urlpatterns = [
    path('', views.bank_advice, name='bank_advice'),
]