from django.contrib import admin
from myApp.models import Employee
from myApp.models import Attendance
from myApp.models import Leave
from myApp.models import Performance

# Register your models here.

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Leave)
admin.site.register(Performance)