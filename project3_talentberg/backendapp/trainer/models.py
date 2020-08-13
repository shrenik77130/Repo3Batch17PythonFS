from django.db import models

class Trainer(models.Model):
    CHOICES=(('1','Male'),('2','Female'))
    
    joindate=models.DateField()
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=11,choices=CHOICES)
    dob=models.DateField()
    address=models.TextField()
    suburb=models.TextField(max_length=100)
    city=models.TextField(max_length=100)
    pincode=models.TextField(max_length=100)
    whatsappno=models.TextField(max_length=100)
    emailid=models.CharField(max_length=100)
    qualification=models.TextField(max_length=100)
    resume=models.FileField(upload_to='resumes/')
    