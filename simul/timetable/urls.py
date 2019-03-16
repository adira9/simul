from django.urls import path

from . import views

app_name="timetable"
urlpatterns = [
    # ex: /polls/
    path('', views.db_home_full, name='dashboard_home'),
    path('?p1?home/', views.db_home, name='db_home'),
    path('timetable/', views.db_tt_full, name='dashboard_tt'),
    path('?p2?tt/', views.db_tt, name='db_tt'),
    path('attendance/', views.db_attend_full, name='dashboard_attend'),
    path('?p3?att/', views.db_attend, name='db_attend'),    

]