from django import forms
from .models import CourseMaster,Course
from certification.models import Certificate
import datetime

class CourseRegistrationForm(forms.ModelForm):
    
    class Meta:
        model=CourseMaster
        fields=('fkcourseid','displayname','duration','fees','fkcertificateid','course_content')
        
        widgets={
        #     'fkcourseid':forms.ModelChoiceField(queryset=Course.objects.all()),
              'displayname':forms.TextInput(attrs={'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control'}),
            'fees':forms.TextInput(attrs={'class':'form-control'}),
        #     'fkcertificateid':forms.ModelChoiceField(queryset=Certificate.objects.all()),
            'course_content':forms.FileInput()
        }
        