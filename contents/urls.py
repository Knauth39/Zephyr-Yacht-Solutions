# contents/urls.py

from django.urls import path 
from .views import ComplianceView, ConciergeView

urlpatterns = [
    path("compliance/", ComplianceView.as_view(), name="compliance"),
    path("concierge/", ConciergeView.as_view(), name="concierge"),
]


