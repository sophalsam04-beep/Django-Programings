  # 1. Model
      # Manage data

from django.db import models

class Student(models.Model):
      name = models.CharField(max_length=100);
      age = models.IntegerField();
      address = models.TextField();
      number = models.FloatField();
      isStudent = models.BooleanField();
      birth_date = models.DateField();
      times = models.DateTimeField(auto_now_add=True);
      emails = models.EmailField(unique=True);
      image = models.ImageField();
      file = models.FileField();
      # Connect table -> one to many
      table = models.ForeignKey();
      
      
      
      def __str__(self):
          return self.name
      
      
      
    

    
    
    