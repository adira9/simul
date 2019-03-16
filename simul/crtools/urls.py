from django.urls import path

from . import views

app_name="crtools"
urlpatterns = [
    # ex: /polls/
    path('timetable/', views.tt_admin_full, name='crtools_tt'),
    path('?p4?admintt/', views.tt_admin, name='cr_tt'),
    path('?p5?adminrem/', views.rem_admin, name='cr_rem'),
    path('reminders/', views.rem_admin_full, name='crtools_rem'),
    
]