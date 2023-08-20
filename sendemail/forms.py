# sendemail/forms.py 

from django import forms 

class ContactForm(forms.Form):
    first_name  = forms.CharField(max_length=100)
    last_name   = forms.CharField(max_length=100)
    email       = forms.EmailField(required=True)
    message     = forms.CharField(widget=forms.Textarea, required=True)

class ZeppelinForm(forms.Form):
    first_name  = forms.CharField(max_length=100)
    last_name   = forms.CharField(max_length=100)
    email       = forms.EmailField(required=True)
    user_type   = forms.CharField()
    company     = forms.CharField(help_text="Name of vessel or company", max_length=200)
    message     = forms.CharField(widget=forms.Textarea, required=True)
