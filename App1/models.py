from django.db import models

# Create your models here.
class CarItem(models.Model):
    name=models.CharField(max_length=50)
    model=models.CharField(max_length=20)
    price=models.IntegerField()
    def __str__(self):
        return self.name
    

class MovItem(models.Model):
    name=models.CharField(max_length=50)
    year=models.IntegerField()
    dir=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    