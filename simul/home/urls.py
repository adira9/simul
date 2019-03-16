from django.urls import path
from . import views

app_name="home"
urlpatterns = [
    # ex: /polls/
    path('', views.display_home, name='homepage'),
    path('login/',views.login_custom ,name='login'),
]