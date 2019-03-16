from django.shortcuts import render,redirect
from django.urls import reverse
import datetime
from .models import Reminder, TTChange
from timetable.models import TTFormat,Course
# Create your views here.


def tt_admin_full(request):
    username=request.session.get('username')
    userid=request.session.get('userid')
    if userid is None:
        return redirect(reverse('home:homepage'))
    context={
        'username':username,
    }
    return render(request, 'crtools/ttadmin_full.html',context)

def tt_admin(request):
    today_date=datetime.datetime.now().date().strftime('%Y-%m-%d')
    context={ 'ttdate':today_date,'today_set':today_date }


    weekday_today=datetime.datetime.strptime(context['ttdate'],"%Y-%m-%d")
    weekday_today=weekday_today.date().weekday()+1
    
    original_tt=TTFormat.objects.filter(day=weekday_today).order_by('start_hour')
    changes_tt=TTChange.objects.filter(date=context['ttdate']).order_by('start_hour','-date')
    

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
    context['day_class']=list(merged_tt)

    if request.method=="POST":
        
        context['ttdate']=request.POST['ttdate']
        
        weekday_today=datetime.datetime.strptime(context['ttdate'],"%Y-%m-%d")
        weekday_today=weekday_today.date().weekday()+1
    
        if weekday_today>5:
            context['errortext']="Please select only a weekday"
            return render(request, 'crtools/tt_admin.html',context)

        

        if 'can_sel' in request.POST:
            context['can']=True
        
        if 'add_sel' in request.POST:
            context['add']=True
        
        courses=Course.objects.filter(course_semester=request.session.get('sem'))
        context['courses']=courses

        if 'canclass' in request.POST:
            for c in merged_tt:
                if c.course_code.course_code == request.POST['class_select']:
                    reference=c
            change=TTChange()
            change.course_code=reference.course_code
            change.start_hour=reference.start_hour
            change.date=datetime.datetime.now().date()
            change.deleted=True
            change.lab_hour=reference.lab_hour
            change.save()

        if 'conchange' in request.POST:
            cc=request.POST['course_add_sel']
            print(cc)
            reference=Course.objects.get(course_code=cc)
            print(reference)
            change2=TTChange()
            change2.course_code=reference
            change2.start_hour=request.POST['hour_add_sel']
            change2.date=datetime.datetime.now().date()
            change2.deleted=False
            if request.POST.get('labconfadd')==True:
                change2.lab_hour=True
            else:
                change2.lab_hour=False
            change2.save()
        
        if 'canchange' in request.POST:
            context['can']=False
            context['add']=False
            context['rep']=False

    
            
            original_tt=TTFormat.objects.filter(day=weekday_today).order_by('start_hour')
            changes_tt=TTChange.objects.filter(date=request.POST['ttdate']).order_by('start_hour','-date')


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
            context['day_class']=list(merged_tt)

    

    return render(request, 'crtools/tt_admin.html',context)

def rem_admin(request):
    today_date=datetime.datetime.now().date().strftime('%Y-%m-%d')
    context={ 'seldate':today_date }
    if request.method=="POST":
        context['seldate']=request.POST['seldate']

        if 'viewr' in request.POST:
            context['view_rem']=True
            reminder_list=Reminder.objects.filter(set_date=request.POST['seldate']).order_by('-creation_date')
            context['rl']=reminder_list

        if 'rem_del' in request.POST:
            context['view_rem']=True
            del_id=request.POST['rem_del']
            Reminder.objects.get(id=del_id).delete()
            context['rl']=Reminder.objects.filter(set_date=request.POST['seldate']).order_by('-creation_date')
            context['view_rem']=True

        if 'addrem' in request.POST:
            context['addrem']=True   

        if "rem_can" in request.POST:
            context['view_rem']=True
        
        if "rem_con" in request.POST:
            new_rem=Reminder()
            new_rem.creation_date=datetime.datetime.now()
            new_rem.set_date=request.POST['seldate']
            new_rem.reminder_text=request.POST['rem_text_stuff']
            new_rem.save()
            context['rl']=Reminder.objects.filter(set_date=request.POST['seldate']).order_by('-creation_date')
            context['view_rem']=True

    return render(request, 'crtools/rem_admin.html',context)

def rem_admin_full(request):
    username=request.session.get('username')
    userid=request.session.get('userid')
    if userid is None:
        return redirect(reverse('home:homepage'))
    context={
        'username':username,
    }         
    
    return render(request, 'crtools/reminders_full.html',context)