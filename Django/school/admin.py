from django.contrib import admin
from school.models import School
from unfold.admin import ModelAdmin as UnfoldModelAdmin
class SchoolAdmin(UnfoldModelAdmin):
    list_display = ['name', 'school_id', 'location']

# Register your models here.
admin.site.register(School, SchoolAdmin)