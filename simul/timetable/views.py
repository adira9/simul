from django.shortcuts import render,redirect
from django.urls import reverse
import datetime
from home.models import Student
from .models import TTFormat,Course,Enrolled
from crtools.models import Reminder,TTChange
# Create your views here.

# HOMEPAGE


def db_home_full(request):
    username=request.session.get('username')
    userid=request.session.get('userid')
    if userid is None:
        return redirect(reverse('home:homepage'))
    context={
        'username':username,
    }
    return render(request, 'timetable/home_full.html',context)

def db_home(request):
    username=request.session.get('username')
    userid=request.session.get('userid')
    if userid is None:
        return redirect(reverse('home:homepage'))
    context={}
    return render(request, 'timetable/home.html', context)



#TIMETABLE

def db_tt_full(request):
    #get the required object - user
    #check for notifications and load
    #
    
    username=request.session.get('username')
    userid=request.session.get('userid')
    if userid is None:
        return redirect(reverse('home:homepage'))
    context={
        'username':username,
    }
    return render(request, 'timetable/timetable_full.html',context)

def db_tt(request):
    userid=request.session.get('userid')
    if userid is None:
        return redirect(reverse('home:homepage'))
    if request.method=="POST":
        context={}
        return render(request, 'timetable/attendance.html', context)

    weekday_today=request.session.get('day')
    
    original_tt=TTFormat.objects.filter(day=weekday_today).order_by('start_hour')
    changes_tt=TTChange.objects.filter(date=datetime.datetime.now().strftime("%Y-%m-%d")).order_by('start_hour','-date')
    

    merged_tt=[]
    for k in range(1,9):
        org=None
        ch=None
        for o in original_tt:
            if o.start_hour==k:
                org=o
                break
        for c in changes_tt:
            if c.start_hour==k:
                ch=c
                break
        if org and ch :
            if not ch.deleted:
                merged_tt.append(ch)
        if org and not ch:
            merged_tt.append(org)
        if ch and not org:
            merged_tt.append(ch)
    merged_tt=list(merged_tt)
    today=datetime.datetime.now().date().strftime('%Y-%m-%d')
    reminders=Reminder.objects.filter(set_date=today)
    
    context={
        'reminders':reminders,
        'classes_list':merged_tt,
        'day':request.session.get('weekday'),
        'date':request.session.get('date'),    
    }
    return render(request, 'timetable/timetable.html', context)


# ATTENDANCE
def db_attend_full(request):
    #get the required object - user
    #check for notifications and load
    #
    
    username=request.session.get('username')
    userid=request.session.get('userid')
    if userid is None:
        return redirect(reverse('home:homepage'))
    context={
        'username':username,
    }
    return render(request, 'timetable/attendance_full.html',context)


def db_attend(request):
    username=request.session.get('username')
    userid=request.session.get('userid')
    if userid is None:
        return redirect(reverse('home:homepage'))
    student=Student.objects.get(rollno=userid)
    courses=Enrolled.objects.filter(student_id=userid)

    if request.method=='POST':
        if 'bunk' in request.POST:
            course_changed=Enrolled.objects.get(course_code=request.POST['bunk'],student_id=student)
            if course_changed.classes_bunked<course_changed.course_code.num_classes:
                course_changed.classes_bunked+=1
            course_changed.save()
        else:
            course_changed=Enrolled.objects.get(course_code=request.POST['unbunk'],student_id=student)
            if course_changed.classes_bunked>0:
                course_changed.classes_bunked-=1
            course_changed.save()
    
    for course in courses:
        course.bunk_percentage=((course.course_code.num_classes-course.official_classes_bunked)/course.course_code.num_classes)*100.0
        course.save()
    context={
        'username':username,
        'courses':courses,
    }
    return render(request, 'timetable/attendance.html', context)
