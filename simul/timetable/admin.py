from django.contrib import admin
from .models import Course, Enrolled, TTFormat

admin.site.register(Course)
admin.site.register(TTFormat)
admin.site.register(Enrolled)

# Register your models here.

