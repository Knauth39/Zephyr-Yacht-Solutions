# zeppelin/forms.py

from django import forms 

POSITION_CHOICES = (
    ("Captain", "Captain"),
    ("Vessel Admin", "Vessel Admin"),
    ("Fleet Manager", "Fleet Manager"),
    ("Yacht Agent", "Yacht Agent"),
    ("Broker", "Broker"),
)

class RequestRegistrationForm(forms.Form):
    first_name  = forms.CharField(max_length = 100)
    last_name   = forms.CharField(max_length = 100)
    email       = forms.EmailField(required = True)
    position    = forms.CharField(max_length = 50, choices = POSITION_CHOICES, required=True)
