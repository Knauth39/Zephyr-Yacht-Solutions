# contents/views.py

from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Compliance, Concierge, Management

class ComplianceView(TemplateView):
    model = Compliance
    template_name = "compliance.html"

class ConciergeView(TemplateView):
    model = Concierge
    template_name = "concierge.html"

class ManagementView(TemplateView):
    model = Management 
    template_name = "management.html"