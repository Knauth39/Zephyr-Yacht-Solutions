# sendemail/forms.py 

from django import forms 

class ContactForm(forms.Form):
    name_first  = forms.CharField(max_length=100)
    name_last   = forms.CharField(max_length=100)
    from_email  = forms.EmailField(required=True)
    message     = forms.CharField(widget=forms.Textarea, required=True)
    '''
    In views.py, impliment an if/else statement to show fields below.
    If is_yacht == True, then display flag_reg and gross_ton
    '''
    #is_yacht    = forms.BooleanField()
    #flag_reg    = forms.CharField(max_length=100)
    #gross_ton   = forms.IntegerField()