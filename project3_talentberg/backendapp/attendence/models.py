from django.db import models
from admission.models import Admission

class AttendenceStatus(models.Model):
    
    status=models.CharField(max_length=100)

class Attendence(models.Model):
    
    att_date = models.DateField()
    fkadmissionid = models.ForeignKey(Admission,on_delete=models.CASCADE),
    status=models.ForeignKey(AttendenceStatus,on_delete=models.CASCADE)
    remark=models.TextField()
    
    
    
