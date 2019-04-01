from django.urls import path
from . import views

app_name="teacher"
urlpatterns = [
    # ex: /polls/
    path('login/',views.teacher_login ,name='login'),
    path('dash/',views.teacher_dash,name="home"),
    path('add/',views.teacher_add,name="add"),
    path("attendance/",views.teacher_attendance,name="attendance")
]