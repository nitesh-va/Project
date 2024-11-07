from django.contrib import admin
from school.models import School
from unfold.admin import ModelAdmin as UnfoldModelAdmin
class SchoolAdmin(UnfoldModelAdmin):
    list_display = ['name', 'school_id', 'location','is_active']

    # def dept_name(self, obj):
    #     return ", ".join(str(related) for related in obj.related_field.all())
    # dept_name.short_description = 'Related Field'






# Register your models here.
admin.site.register(School, SchoolAdmin)