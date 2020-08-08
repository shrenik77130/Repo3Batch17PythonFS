from django.db import models
from enquiry.models import Enquiry
from batch.models import Batch
from trainer.models import Trainer

class AdmissionStatus(models.Model):
    status=models.CharField(max_length=100)
    
class Admission(models.Model):
    
    status=models.ForeignKey(AdmissionStatus,on_delete=models.CASCADE)
    admndate=models.DateField()
    fkenqid=models.ForeignKey(Enquiry,on_delete=models.CASCADE)
    fkbatchid=models.ForeignKey(Batch,on_delete=models.CASCADE)
    fktrainerid=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    coursefees=models.FloatField()
    receivedfees=models.FloatField()
    pendingfees=models.FloatField()
    
    
