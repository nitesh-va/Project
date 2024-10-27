from django.contrib import admin
from teacher.models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'emp_id', 'performance','dept_name','school_name']

admin.site.register(Teacher, TeacherAdmin)