from django.db import models

# Create your models here.
class Cls(models.Model):
   name = models.CharField(max_length=30)
   section = models.CharField(max_length=30)
 
   def __str__(self):
       return self.name