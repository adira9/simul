from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Student
from timetable.views import db_home_full
from urllib import request
import datetime
import calendar

# Create your views here.

def display_home(request):
    request.session.delete()
    context={}
    return render(request, 'home/index.html', context)

def login_custom(request):
    request.session.flush()
    if request.method=='POST':
        context={}
        username=request.POST['login_email']
        password=request.POST['pwd_login']
        try:
            user=Student.objects.get(username=username)
        except:
            context['errormessage']="This user is not registered"
            return render(request, 'home/login.html', context)
        
        if password!=user.password:
            context['errormessage']="Password doesn't match"
            return render(request, 'home/login.html', context)
        #response = db_home_full(request,context)
        #return response
        today=datetime.datetime.now()
        request.session['username']=user.name
        request.session['userid']=user.rollno
        request.session['sem']=user.semester
        request.session['day']=today.weekday()+1
        request.session['date']=today.strftime(" %d-%m-%y")
        request.session['weekday']=calendar.day_name[today.weekday()]
        return redirect(reverse('timetable:dashboard_home'))
    else:
        context={}
        return render(request, 'home/login.html', context)
