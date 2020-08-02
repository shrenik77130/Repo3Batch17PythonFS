from django.db import models
from certification.models import Certificate

class Course(models.Model):
    coursename=models.CharField(max_length=100)
    
    def __str__(self):
        return self.coursename
    
    
class CourseMaster(models.Model):
    fkcourseid = models.ForeignKey(Course,on_delete=models.CASCADE)
    displayname = models.TextField(max_length=100)
    duration = models.IntegerField()
    fees = models.FloatField()
    fkcertificateid=models.ForeignKey(Certificate,on_delete=models.CASCADE)
    course_content = models.FileField(upload_to='syllabus/')
    
    
    
'''  
Scenario 1
=======================
    
    
Course                                              CourseMaster
--------                                            --------------------------
courseid    coursename                              cmid  fkcourseid   display_name              duration 
1           Data Analysis                             1      1         Data Analsysis 2020        20 days
                                                      2      1         Data Analsysis 2021        30 Days


Scenario 2
=======================

Course
------
courseid       coursename        duration
1              Data Analysis     30 days


Student
--------
admndate         name        fkcourseid        duration
2 aug 2020       nitin           1              20 Days
1 jan 2021       yogesh          1              30 days

'''
