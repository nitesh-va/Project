from django.db import models
from django.utils import timezone
from department.models import Department
from school.models import ActiveManager
 


def update_teacher_performance(teacher):
    """Update teacher's performance based on their students' pass percentage."""
    students = Student.objects.filter(emp_id=teacher)
    total_students = students.count()

    if total_students > 0:
        total_passed = students.filter(percentage__gte=33.0).count()  # Assuming 33 is the passing mark
        pass_percentage = (total_passed / total_students) * 100
    else:
        pass_percentage = 0.0  # No students means 0% performance
    
    # Update the teacher's performance
    teacher.performance = pass_percentage
    teacher.save()  # Save the changes


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(primary_key=True)
    maths_marks = models.IntegerField()
    physics_marks = models.IntegerField()
    chemistry_marks = models.IntegerField()
    #class_teachers = models.CharField(max_length=100, default=False)  # Directly storing teacher's name
    total_marks = models.IntegerField(default=0)
    percentage = models.FloatField(default=0.0)
    emp_id = models.ForeignKey('teacher.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    dept_name=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    
    objects = models.Manager()
    active = ActiveManager()

    def save(self, *args, **kwargs):
        """Override save to calculate total marks and percentage before saving."""
        self.total_marks = self.maths_marks + self.physics_marks + self.chemistry_marks
        self.percentage = (self.total_marks / 300) * 100 if self.total_marks > 0 else 0.0
        
        super().save(*args, **kwargs)  # Save the student first

        # After saving the student, update the teacher's performance
        if self.emp_id:
            update_teacher_performance(self.emp_id)

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_no})"