# accounts/urls.py

from django.urls import path 
from .views import CustomUserView

urlpatterns = [
    path("client/", CustomUserView.as_view(), name="client")
]