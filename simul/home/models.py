from django.db import models

class Student(models.Model):

    name=models.CharField(max_length=40)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    rollno=models.IntegerField()
    rollno.primary_key=True
    classid=models.CharField(max_length=10)
    semester=models.IntegerField()
    last_online=models.DateField(auto_now=True)
    cr=models.BooleanField()
    dev_id=models.CharField(max_length=40)

# Create your models here.
