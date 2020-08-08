from django.db import models
from course.models import CourseMaster
from admission.models import Admission

class QuestionType(models.Model):
    
    quetiontype=models.CharField(max_length=100)
    
class QuestionBank(models.Model):
    
    fkcoursemasterid=models.ForeignKey(CourseMaster,on_delete=models.CASCADE)
    questioncode=models.IntegerField()
    fkquestiontypeid=models.ForeignKey(QuestionType,on_delete=models.CASCADE)
    title=models.TextField()
    optiona=models.TextField()
    optionb=models.TextField()
    optionc=models.TextField()
    optiond=models.TextField()
    ans=models.TextField()
    
class ExamType(models.Model):
    
    examtype=models.CharField(max_length=100)
    
class ExamMaster(models.Model):
    
    fkexamtypeid = models.ForeignKey(ExamType,on_delete=models.CASCADE)
    examdate = models.DateField()
    fkcoursemasterid = models.ForeignKey(CourseMaster,on_delete=models.CASCADE)
    totalmarks=models.IntegerField()
    totaltime=models.FloatField()
    
class ExamLog(models.Model):
    
    fkexam_masterid=models.ForeignKey(ExamMaster,on_delete=models.CASCADE)
    fkadmissionid=models.ForeignKey(Admission,on_delete=models.CASCADE)
    scoredmarks=models.IntegerField()
    result=models.CharField(max_length=100)
    
    
    
    
    
