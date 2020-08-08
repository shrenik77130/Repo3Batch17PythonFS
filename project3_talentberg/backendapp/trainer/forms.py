from django import forms

class RawTrainerForm(forms.Form):
    joindate  = forms.DateField(label="Select Join Date")
    
    fname = forms.CharField(label="First Name",required=True)
    mname = forms.CharField(label="Middle Name",required=True)
    lname = forms.CharField(label="Last Name",required=True)
    