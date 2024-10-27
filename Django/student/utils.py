from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student 



def cutoff_cleared(cutoff_percentage):
    """Retrieve students who have a percentage above the cutoff."""
    return Student.objects.filter(percentage__gte=cutoff_percentage)

def cutoff_notcleared(cutoff_percentage):
    """Retrieve students who have a percentage below the cutoff."""
    return Student.objects.filter(percentage__lt=cutoff_percentage) 
