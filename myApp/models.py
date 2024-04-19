from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    employment_start_date = models.DateField()
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Default value set to 0.0

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.clock_in}"

class LeaveBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_leave_days = models.IntegerField(default=0)

    def __str__(self):
        return f"Leave Balance for {self.user.username}"

class Leave(models.Model):
    LEAVE_TYPES = (
        ('vacation', 'Vacation'),
        ('sick', 'Sick Leave'),
        ('maternity', 'Maternity/Paternity Leave'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_requests')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='pending')
    reason = models.TextField()
    approved_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leave_requests')
    rejection_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"

class LeaveHistory(models.Model):
    leave = models.ForeignKey(Leave, on_delete=models.CASCADE)
    leave_balance = models.ForeignKey(LeaveBalance, on_delete=models.CASCADE)

    def __str__(self):
        return f"Leave History: {self.leave.employee} - {self.leave.leave_type}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances_received')
    goal = models.TextField()
    progress = models.TextField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    evaluation_date = models.DateField()
    performance_rating = models.PositiveIntegerField(default=0)
    reviewer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='performances_reviewed')

    def __str__(self):
        return f"{self.employee} - {self.evaluation_date}"
