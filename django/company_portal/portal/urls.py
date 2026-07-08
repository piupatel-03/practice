from django.urls import path
from . import views


urlpatterns = [
    path('employees/', views.employee_list, name='employee-list'),
    path('departments/', views.department_list, name='department-list'),
    path('projects/', views.project_list, name='project-list'),
    path('create-employee/', views.create_employee),
    path('employees/<int:emp_id>/', views.get_employee, name='get-employee'),
    path('employees/age/<int:age>/', views.employees_by_age, name='filter-employees-by-age'),
    path('exclude-employees/<int:age>/', views.exclude_employees, name='exclude-employees'),
    path('update-employee/<int:emp_id>/', views.update_employee, name='update-employee'),
    path('delete-employee/<int:emp_id>/', views.delete_employee, name='delete-employee'),
    path('employees/above-age/<int:age>/', views.employees_above_age, name='employees-above-age'),
    path('employees/count/', views.employee_count, name = 'employee-count'),
    path('employees/average-age/', views.average_age, name = 'average-age'),
    path('employees/total-age/', views.total_age, name = 'total-age'),
    path('employees/max-age/', views.maximum_age, name = 'max-age'),
    path('employees/min-age/', views.minimum_age, name = 'min-age'),
    path('department/<int:dept_id>/employees/',views.department_employees,name='department-employees'),
    path('employee/<int:emp_id>/projects/',views.employee_projects,name='employee-projects'),
    path('employee/<int:emp_id>/profile/',views.employee_profile,name='employee-profile'),
    path('employees/order/name/', views.employees_by_name),
    path('reports/projects/',views.project_allocation_report,name='project-report'),
    

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),


]