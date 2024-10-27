from django.contrib import admin
from student.models import Student
from unfold.admin import ModelAdmin as UnfoldModelAdmin
# Register your models here.
class StudentAdmin(UnfoldModelAdmin):
    list_display = ['name', 'roll_no', 'maths_marks','physics_marks','chemistry_marks','total_marks','percentage','emp_id','dept_name']


admin.site.register(Student,StudentAdmin)