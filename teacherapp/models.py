from django.db import models


# Create your models here.
class Teacher(models.Model):
    
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    course_code = models.CharField(max_length=20)
   
    def __str__(self):
        
        return self.name

