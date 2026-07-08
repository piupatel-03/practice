from django.http import JsonResponse
from .models import Employee, Department, Project
from django.db.models import Count, Avg, Sum, Max, Min
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    username = request.GET.get("username")
    password = request.GET.get("password")

    user = authenticate(
        username=username, password=password
    )

    if user is not None:
        login(request, user)
        return JsonResponse({
            "message": "Login successful",
            "username": user.username 
        })
    
    return JsonResponse({
        "error": "Invalid username or password"
    }, status=401)


def logout_user(request):
    logout(request)

    return JsonResponse({
        "message": "Logout successful"
    })









# Employee List
def employee_list(request):
    employees = Employee.objects.all()

    data = []

    for emp in employees:
        data.append({
            "id": emp.id,
            "name": emp.name,
            "age": emp.age,
            "email": emp.email,
            "department": emp.department.name,
        })

    return JsonResponse(data, safe=False)


# Get Single Employee
def get_employee(request, emp_id):
    try:
        employee = Employee.objects.get(id=emp_id)

        data = {
            "id": employee.id,
            "name": employee.name,
            "age": employee.age,
            "email": employee.email,
            "department": employee.department.name,
        }

        return JsonResponse(data)

    except Employee.DoesNotExist:
        return JsonResponse(
            {"error": "Employee not found"},
            status=404
        )
    


def exclude_employees(request,age):
    employees = Employee.objects.exclude(age=age)

    data = []

    for emp in employees:
        data.append({
            "id": emp.id,
            "name": emp.name,
            "age": emp.age,
            "email": emp.email,
            "department" : emp.department.name,
        })
    
    return JsonResponse(data, safe=False)

def employees_by_age(request, age):
    employees = Employee.objects.filter(age=age)

    data = []

    for emp in employees:
        data.append({
            "id": emp.id,
            "name": emp.name,
            "age": emp.age,
            "department": emp.department.name,
        })
    
    return JsonResponse(data, safe=False)

def employees_above_age(request, age):
    employees = Employee.objects.filter(age__gt=age)

    data = []

    for emp in employees:
        data.append({
            "id": emp.id,
            "name": emp.name,
            "age": emp.age,
            "email": emp.email,
            "department": emp.department.name,
        })

    return JsonResponse(data, safe=False)

def update_employee(request, emp_id):
    updated = Employee.objects.filter(id=emp_id).update(
        age=30,
        email="upadate@gmail.com"
    )

    if updated:
        return JsonResponse({
            "message": "Employee updated successfully"})
    
    return JsonResponse({
        "error": "Employee not found"},
        status=404
    )

def employee_count(request):
    total = Employee.objects.count()

    return JsonResponse({
        "Total Employees": total 
    })

def average_age(request):
    result = Employee.objects.aggregate(Avg('age'))

    return JsonResponse(result)

def total_age(request):
    result = Employee.objects.aggregate(Sum('age'))

    return JsonResponse(result)

def maximum_age(request):
    result = Employee.objects.aggregate(Max('age'))

    return JsonResponse(result)

def minimum_age(request):
    
    result = Employee.objects.aggregate(Min('age'))

    return JsonResponse(result)

def delete_employee(request, emp_id):
    deleted, _ = Employee.objects.filter(id=emp_id).delete()

    if deleted:
        return JsonResponse({
            "message": "Employee deleted successfully"
        })
    
    return JsonResponse({
        "error": "Employee not found"
    }, status=404)

def employee_projects(request, emp_id):
    employee = Employee.objects.get(id=emp_id)

    data = {
        "employee": employee.name,
        "projects": []
    }

    for project in employee.projects.all():
        data["projects"].append({
            "id": project.id,
            "name": project.name,
        })

    return JsonResponse(data)

def employee_profile(request, emp_id):
    employee = Employee.objects.get(id=emp_id)

    data = {
        "employee": employee.name,
        "phone": employee.profile.phone,
        "address": employee.profile.address,
    }

    return JsonResponse(data)

def employees_by_name(request):
    employees = Employee.objects.order_by("name")

    data = []

    for emp in employees:
        data.append({
            "id": emp.id,
            "name": emp.name,
            "age": emp.age,
        })

    return JsonResponse(data, safe=False)

# Department List
def department_list(request):
    departments = Department.objects.all()

    data = []

    for dept in departments:
        data.append({
            "id": dept.id,
            "name": dept.name,
            "code": dept.code,
            "location": dept.location,
        })

    return JsonResponse(data, safe=False)

def department_employees(request, dept_id):
    department = Department.objects.get(id=dept_id)

    data = {
        "department": department.name,
        "employees": []
    }

    for employee in department.employees.all():
        data["employees"].append({
            "id": employee.id,
            "name": employee.name,
            "age": employee.age,
        })

    return JsonResponse(data)

# Project List
def project_list(request):
    projects = Project.objects.all()

    data = []

    for project in projects:
        data.append({
            "id": project.id,
            "name": project.name,
            "description": project.description,
        })

    return JsonResponse(data, safe=False)

def project_allocation_report(request):
    employees = Employee.objects.all()

    data = []

    for emp in employees:
        projects = []

        for project in emp.projects.all():
            projects.append({
                "id": project.id,
                "name": project.name,
            })

        data.append({
            "employee": emp.name,
            "projects": projects,
        })

    return JsonResponse(data, safe=False)

# ORM create()
def create_employee(request):
    department = Department.objects.get(id=1)

    employee = Employee.objects.create(
        name="Priyanshi",
        age=23,
        email="priya@gmail.com",
        department=department
    )

    return JsonResponse({
        "message": "Employee created successfully",
        "employee_id": employee.id
    })