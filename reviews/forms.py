# reviews/forms.py
from django import forms

class WriteReview(forms.Form):
    author      = forms.CharField(max_length=150)
    position    = forms.CharField(max_length=150)
    company     = forms.CharField(max_length=150)
    review      = forms.CharField(widget=forms.Textarea, required=True)
    publish     = forms.BooleanField()