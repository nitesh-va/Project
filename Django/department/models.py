from django.db import models
from school.models import School
from django.utils import timezone
from teacher.models import Teacher
# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100, null=True, blank=True)
    dept_id = models.IntegerField(primary_key=True)  # Ensure this is defined
    hod = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name
    