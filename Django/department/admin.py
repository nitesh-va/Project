from django.contrib import admin
from department.models import Department
from unfold.admin import ModelAdmin as UnfoldModelAdmin
# Register your models here.
class DepartmentAdmin(UnfoldModelAdmin):
    list_display = ['department_name', 'dept_id','hod','school']

admin.site.register(Department, DepartmentAdmin)  