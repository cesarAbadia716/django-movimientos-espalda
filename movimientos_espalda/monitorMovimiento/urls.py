# monitoreo_espalda/urls.py
from django.urls import path
from .views import socket_client

urlpatterns = [
    path('socket_client/', socket_client, name='socket_client'),
]
