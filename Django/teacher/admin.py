from django.contrib import admin
from teacher.models import Teacher
from unfold.admin import ModelAdmin as UnfoldModelAdmin
# Register your models here.
class TeacherAdmin(UnfoldModelAdmin):
    list_display = ['name', 'emp_id', 'performance','dept_name','school_name','is_active']

admin.site.register(Teacher, TeacherAdmin)