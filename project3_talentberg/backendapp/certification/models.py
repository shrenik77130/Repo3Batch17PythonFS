from django.db import models

class Certificate(models.Model):
    
    institute=models.CharField(max_length=100)
    atc_code=models.CharField(max_length=100)
    regdate=models.DateField()
    
    def __str__(self):
        return self.institute
