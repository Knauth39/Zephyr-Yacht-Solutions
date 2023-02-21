# sendemail/forms.py 

from django import forms 

class ContactForm(forms.Form):
    name_first  = forms.CharField(max_length=100)
    name_last   = forms.CharField(max_length=100)
    from_email  = forms.EmailField(required=True)
    message     = forms.CharField(widget=forms.Textarea, required=True)
    is_yacht    = forms.BooleanField()
    flag_reg    = forms.CharField(max_length=100)
    gross_ton   = forms.IntegerField()