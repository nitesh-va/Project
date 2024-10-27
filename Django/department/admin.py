from django.contrib import admin
from department.models import Department
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'dept_id','hod','school']

admin.site.register(Department, DepartmentAdmin)  