from django import forms
from myApp.models import Employee
from .models import Attendance, Leave, LeaveBalance, LeaveHistory

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'

class LeaveBalanceForm(forms.ModelForm):
    class Meta:
        model = LeaveBalance
        fields = '__all__'

class LeaveHistoryRecord(forms.ModelForm):
    class Meta:
        model = LeaveHistory
        fields = '__all__'
