# zeppelin/urls.py

from django.contrib import admin 
from django.urls import path 

from .views import requestRegistrationView, successView

urlpatterns = [
    path("client/", requestRegistrationView, name="client"),
    path("success/", successView, name="success"),
]