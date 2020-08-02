from django.db import models

    
class Catagory(models.Model):
    
    catagoryname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.catagoryname
    
class Menu(models.Model):
    
    foodname = models.CharField(max_length=100)
    foodtaste = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to="pics")
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    fkcatagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    
    