from django.db import models

class TeacherAcc(models.Model):
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    
# Create your models here.
