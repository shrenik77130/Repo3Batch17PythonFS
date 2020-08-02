from django.db import models
from student.models import Student
from course.models import CourseMaster


class Status(models.Model):
    status=models.CharField(max_length=100)
    
class Enquiry(models.Model):
    fkstatusid=models.ForeignKey(Status,on_delete=models.CASCADE)
    enqdate=models.DateField()
    fkstudid=models.ForeignKey(Student,on_delete=models.CASCADE)
    fkcourseid=models.ForeignKey(CourseMaster,on_delete=models.CASCADE)
    batchtime=models.CharField(max_length=100)
    remark=models.TextField()
    
