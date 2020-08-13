from django import forms
from .models import Trainer
import datetime

class TrainerRegistrationForm(forms.ModelForm):
    
    class Meta:
        model=Trainer
        fields=('joindate','fname','mname','lname','gender','dob','address','suburb','city','pincode','whatsappno','emailid','qualification','resume')
        
        
        
        widgets={
            'joindate':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'mname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(),
            'dob':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'suburb':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'whatsappno':forms.TextInput(attrs={'class':'form-control'}),
            'emailid':forms.EmailInput(attrs={'class':'form-control','type':'email'}),
            'qualification':forms.TextInput(attrs={'class':'form-control'}),
            'resume':forms.FileInput(attrs={'type':'file'})
        }

    def clean_joindate(self,*args, **kwargs):
        joindate=self.cleaned_data.get("joindate")
        
        if joindate == "":
            raise forms.ValidationError("This is not Valid Join Date")
        