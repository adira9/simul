from django.db import models
from home.models import Student

class Course(models.Model):
    
    course_name=models.CharField(max_length=40)
    class_id=models.CharField(max_length=10)
    course_code=models.CharField(max_length=10)
    course_code.primary_key=True
    course_semester=models.IntegerField(default=0)
    course_credits=models.IntegerField(default=0)
    lectures=models.IntegerField(default=0)
    labs=models.IntegerField(default=0)
    num_classes=models.IntegerField(default=1)

class Enrolled(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    course_code=models.ForeignKey(Course,on_delete=models.CASCADE)
    classes_bunked=models.IntegerField(default=0)
    bunk_percentage=models.FloatField(default=0)

class TTFormat(models.Model):
    course_code=models.ForeignKey(Course,on_delete=models.CASCADE)
    start_hour=models.IntegerField(default=0)
    day=models.IntegerField(default=0)
    lab_hour=models.BooleanField(default=False)


# Create your models here.
