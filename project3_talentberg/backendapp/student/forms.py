from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = [
            "fname",
            "mname",
            "lname",
            "gender",
            "dob",
            "address",
        ]