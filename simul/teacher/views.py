from django.shortcuts import render,redirect
from .models import TeacherAcc
from django.urls import reverse
from urllib import request
from home.models import Student
from timetable.models import Course,Enrolled
import bluetooth
# Create your views here.

def teacher_login(request):
    request.session.flush()
    context={}
    if request.method=='POST':
        username=request.POST['login_email']
        password=request.POST['pwd_login']
        try:
            user=TeacherAcc.objects.get(username=username)
        except:
            context['errormessage']="This user is not registered"
            return render(request, 'teacher/teacher_login.html', context)
        
        if password!=user.password:
            context['errormessage']="Password doesn't match"
            return render(request, 'home/login.html', context)
        #response = db_home_full(request,context)
        #return response
        request.session['username']=user.name
        request.session['userid']=user.id
        return redirect(reverse('teacher:home'))
   
    return render(request,'teacher/teach_login.html',context)

def teacher_dash(request):
    username=request.session.get('username')
    userid=request.session.get('userid')
    if userid is None:
        return redirect(reverse('teacher:login'))
    context={
        'username':username,
    }
    return render(request,'teacher/teach_dash.html',context)

def teacher_add(request):
    username=request.session.get('username')
    userid=request.session.get('userid')
    # if userid is None:
    #     return redirect(reverse('teacher:login'))
    context={
        'username':username,
    }
    if request.method=="POST":
        if 'fstudent' in request.POST:
            try:
                user=Student.objects.get(rollno=int(request.POST['rno']))
                context['student_roll']=user.rollno
                context['student_name']=user.name
                context['student_sem']=user.semester
                context['student_dev_id']=user.dev_id
                context['found_student']=True
            except:
                context['error']=True
                return render(request,'teacher/teach_add.html',context)
        
        if 'updateid' in request.POST:
            user=Student.objects.get(rollno=int(request.POST['updateid']))  
            user.dev_id=request.POST['dev-id']
            user.save()
            context['student_roll']=user.rollno
            context['student_name']=user.name
            context['student_sem']=user.semester
            context['student_dev_id']=user.dev_id
            context['found_student']=True
            context['success']=True
    
    return render(request,'teacher/teach_add.html',context)

present_students=[]
course_cd=None
absent_students=[] 
def teacher_attendance(request):
    global present_students, absent_students,course_cd
    context={}
    username=request.session.get('username')
    #userid=request.session.get('userid')
    userid=1
    courses=Course.objects.filter(teacher=userid)
    context['courses']=courses
    
    if 'selcourse' in request.POST:
        context['att_success']=True
        
        course=Course.objects.get(course_code= request.POST['course_add_sel'])
        course.num_classes+=1
        course.save()
        course_cd=request.POST['course_add_sel']
        all_students=Enrolled.objects.filter(course_code= request.POST['course_add_sel'])
        
        nearby_devices = bluetooth.discover_devices(duration=4,lookup_names=True, flush_cache=True, lookup_class=False)
        
        for addr, name in nearby_devices:
            try:
                student_by_addr=Student.objects.get(dev_id=str(addr))
                present_students.append(student_by_addr)
            except:
                continue
        
        for student in all_students:
            if student.student_id not in present_students:
                absent_students.append(student.student_id)
        
        context['absentees']=absent_students
        
    if 'end_att' in request.POST:
        marked_present=request.POST.getlist('checks[]')
        course_code=course_cd
        for stu in marked_present:
            st=Student.objects.get(rollno=int(stu))
            present_students.append(st)
            absent_students.remove(st)
        print(absent_students)
        for stu in absent_students:
            print(stu.name)

            enr_up=Enrolled.objects.get(student_id=stu,course_code=course_code)
            print(enr_up)
            enr_up.classes_bunked+=1
            enr_up.official_classes_bunked+=1
            enr_up.save()
        context['att_complete']=True

    # if userid is None:
    #     return redirect(reverse('teacher:login'))
    return render(request,'teacher/teach_attendance.html',context)