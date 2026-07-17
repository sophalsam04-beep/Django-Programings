     # Model
       # Present about database table
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200);
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    
class Student(models.Model):
    name = models.CharField(max_length=200);
    age = models.DecimalField(max_digits=12, decimal_places=2);
    
    
    
    
    