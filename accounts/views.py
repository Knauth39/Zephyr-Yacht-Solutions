from django.shortcuts import render
from django.views.generic import ListView
from .models import CustomUser

class CustomUserView(ListView):
    model = CustomUser
    template_name = "client.html"
