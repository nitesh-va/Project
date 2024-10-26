from django.db import models 
from django.utils import timezone

from school.models import School

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField(primary_key=True)
    performance = models.FloatField(default=0.0)
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    dept_name=models.ForeignKey('department.Department', on_delete=models.DO_NOTHING, null=True, blank=True)
    school_name=models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True, blank=True)
    

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id})"
