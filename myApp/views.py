from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError
from .models import Employee, Attendance, Leave, Performance, LeaveHistory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm, AttendanceForm, LeaveForm, LeaveBalanceForm

def check(request):
    return render(request, 'check.html')

from .models import Employee  # Import the Employee model

def employee_form_view(request):
    employees = Employee.objects.all()  # Fetch all employees from the database
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('employee_list')
            except Exception as e:
                # Log the exception or handle it appropriately
                return HttpResponseServerError("An error occurred while saving the form data.")
        else:
            # Form is not valid, render the form again with validation errors
            return render(request, 'employee_form.html', {'form': form, 'employees': employees})
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form, 'employees': employees})    

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def attendance_form_view(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')  # Redirect to the attendance list view after successful form submission
    else:
        form = AttendanceForm()

    # Render the attendance form template with the form
    return render(request, 'attendance_form.html', {'form': form})

from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractYear
from django.utils.timezone import now

def attendance_list(request):
    # Get the current year
    current_year = now().year
    
    # Get the start and end dates of the current year
    start_of_year = now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    end_of_year = now().replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
    
    # Fetch attendance records for the current year
    attendances = (
        Attendance.objects
        .filter(clock_in__range=(start_of_year, end_of_year))
        .annotate(year=ExtractYear('clock_in'), month=ExtractMonth('clock_in'))
        .values('employee__id', 'employee__first_name', 'employee__last_name', 'year', 'month')
        .annotate(days_present=Count('clock_in'))
        .order_by('year', 'month')
    )
    
    # Get the current month name
    current_month = now().strftime('%B')
    
    return render(request, 'attendance_list.html', {'attendances': attendances, 'current_month': current_month})


# login_required
from .forms import LeaveHistoryRecord

def leave_history_view(request):
    # Retrieve current and historical records
    current_records = Leave.objects.filter(status='pending')  # Modify the filter condition as needed
    historical_records = Leave.objects.exclude(status='pending')  # Modify the filter condition as needed

    # Render the template with the data
    return render(request, 'leave_history.html', {'current_records': current_records, 'historical_records': historical_records})


def leave_form_view(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to leave history or another appropriate page
            return redirect('leave_history')
    else:
        form = LeaveForm()
    return render(request, 'leave_form.html', {'form': form})

def leave_balance_view(request):
    if request.method == 'POST':
        form = LeaveBalanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success URL
    else:
        form = LeaveBalanceForm()
    
    return render(request, 'leave_balance.html', {'form': form})

def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'performance_list.html', {'performances': performances})

def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to index page after successful login
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')


def logout_view(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        # Process the feedback here
        
        # Logout the user
        logout(request)
        return redirect('index')  # Redirect to the homepage after logout
    return render(request, 'logout.html')