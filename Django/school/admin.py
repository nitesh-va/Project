from django.contrib import admin
from school.models import School
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'school_id', 'location']
# Register your models here.
admin.site.register(School, SchoolAdmin)