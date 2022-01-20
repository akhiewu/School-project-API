from django.db import models



class Teacher(models.Model):
    
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    course_code = models.CharField(max_length=20)
   
    def __str__(self):
        
        return self.name

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=30)
    cls = models.CharField(max_length=30)
    roll = models.CharField(max_length=30)
    teacher_select= models.ForeignKey(Teacher, on_delete = models.SET_NULL, null=True)
 
   
    def __str__(self):
        
        return self.name