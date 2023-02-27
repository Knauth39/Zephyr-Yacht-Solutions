# contents/urls.py

from django.urls import path 
from .views import ComplianceView, ConciergeView, ManagementView

urlpatterns = [
    path("compliance/", ComplianceView.as_view(), name="compliance"),
    path("concierge/", ConciergeView.as_view(), name="concierge"),
    path("management/", ManagementView.as_view(), name="management")
]


