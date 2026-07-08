from django.contrib import admin
from .models import Department, Project, Employee, Attendance, EmployeeProfile 

# Register your models here.

admin.site.register(Department)
admin.site.register(Project)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "age",
        "email",
        "department",
        "employee_status",
    )

    list_filter = (
        "department",
    )

    search_fields = (
        "name",
        "email",
    )


    @admin.display(description="Status")
    def employee_status(self, obj):
        if obj.is_active:
            return "Active"
        return "Deactivated"


admin.site.register(Attendance)
admin.site.register(EmployeeProfile)