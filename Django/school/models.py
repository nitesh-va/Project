from django.db import models
from django.utils import timezone

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def count(self):
        return self.get_queryset().count()
    
    def is_active(self):
        return self.get_queryset().filter(is_active=True)
    
    def is_inactive(self):
        return self.get_queryset().filter(is_active=False)

def formatted_departments(self, obj):
        # Fetch active departments linked to the school
        departments = obj.dept_name.filter(is_active=True)  # Adjust based on your field name
        # Create a formatted string for department names and IDs
        dept_list = [f"{department.department_name} (ID: {department.dept_id})" for department in departments]
        return ' '.join(dept_list) if dept_list else 'No active departments'

        formatted_departments.short_description = 'Dept name *' 

class School(models.Model):
    name = models.CharField(max_length=100)  # School name
    school_id = models.IntegerField(primary_key=True)  # Primary key
    location = models.CharField(max_length=255)  # School location
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    dept_name=models.ManyToManyField('department.Department',related_name='school_department', blank=True)

    objects = models.Manager()
    active = ActiveManager()

    def __str__(self):
        return f"{self.name} (ID: {self.school_id})"