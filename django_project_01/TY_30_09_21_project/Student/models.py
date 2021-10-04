from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Student_information(models.Model):
    Name = models.CharField(max_length=30)
    RollNo = models.CharField(max_length=30)
    Branch = models.CharField(max_length=30)
    CGPA = models.CharField(max_length=30)
   

def __str__(self):
        return '%s --%s--%s' % (self.Name,self.Branch, self.RollNo, self.CGPA)
    
        
    
    
    
    