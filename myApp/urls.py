from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name= 'login'),
    path('index', views.index, name= 'index'),    
    path('employee_list/', views.employee_list, name='employee_list'),
    path('attendance_list/', views.attendance_list, name='attendance_list'),
    path('leave_form/', views.leave_form_view, name='leave_form'),
    path('leave_balance/', views.leave_balance_view, name='leave_balance'),
    path('leave_history/', views.leave_history_view, name='leave_history'),
    path('performance/', views.performance_list, name='performance_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('employee_form/', views.employee_form_view, name='employee_form'),
    path('check/', views.check, name = 'check'),
    path('attendance_form', views.attendance_form_view, name='attendance_form'),

]
