# zeppelin/urls.py

from django.contrib import admin 
from django.urls import path 

from .views import contactView, successView 

urlpatterns = [
    path("client/", contactView, name="client"),
    path("success/", successView, name="success"),
]