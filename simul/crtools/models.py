from django.db import models
from timetable.models import Course
# Create your models here.


class Reminder(models.Model):
    creation_date=models.DateTimeField()
    set_date=models.DateTimeField()
    reminder_text=models.TextField()

class Notif(models.Model):
    creation_time=models.DateTimeField()
    message=models.TextField()

class TTChange(models.Model):
    course_code=models.ForeignKey(Course,on_delete=models.CASCADE)
    start_hour=models.IntegerField(default=0)
    date=models.DateTimeField()
    deleted=models.BooleanField(default=False)
    lab_hour=models.BooleanField(default=False)