from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TeacherSerializer

from teacher import models
from student.models import Student

from .utils import get_teacher_performance
# Create your views here.
class TeacherViews(APIView):
    def get(self,request):
        teachers=models.Teacher.objects.all()    
        serializer=TeacherSerializer(teachers,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherByIdView(APIView):
    def get(self, request, emp_id):
            teacher = models.Teacher.objects.get(emp_id=emp_id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
    
    def put(self, request, emp_id):
            teacher = models.Teacher.objects.get(emp_id=emp_id)
            serializer = TeacherSerializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, emp_id):
            teacher = models.Teacher.objects.get(emp_id=emp_id)
             # Delete the student instance
            teacher.delete() 
            return Response(status=status.HTTP_204_NO_CONTENT)
    
class TeacherPerformance(APIView):
    def get(self, request):
        return Response(get_teacher_performance())


class PassedFailedStudentsCountView(APIView):
    def get(self, request):
        passing_percentage = 33.0
        
        # Initialize a dictionary to hold results
        results = {}

        # Get all students and categorize them by teacher's emp_id
        for student in Student.objects.all():
            teacher_emp_id = student.emp_id.emp_id  # Accessing emp_id from the ForeignKey

            if teacher_emp_id not in results:
                results[teacher_emp_id] = {
                    'passed': 0,
                    'failed': 0
                }

            if student.percentage >= passing_percentage:
                results[teacher_emp_id]['passed'] += 1
            else:
                results[teacher_emp_id]['failed'] += 1
        
        return Response(results)
    
class TeacherActiveStudentsView(APIView):
    def get(self, request, emp_id):
            # Retrieve the all the active teacher based on emp_id
            #teacher = models.Teacher.active.is_active().get(emp_id=emp_id)
            # Get active students under this teacher
            active_students = Student.active.is_active().filter(emp_id__emp_id=emp_id,emp_id__is_active=True).values()
            inactive_students = Student.active.is_inactive().filter(emp_id__emp_id=emp_id,emp_id__is_active=True).values()
    
            # Prepare response data
            response_data = {
                'active_students': active_students,
                'inactive_students': inactive_students,             
            }
            
            return Response(response_data, status=200)
            


class ActiveTeacherDetailView(APIView):
    def get(self, request):
            # Retrieve the teacher based on emp_id, ensuring they are active
            teachers= models.Teacher.active.is_active()
            serializer=TeacherSerializer(teachers,many=True)
            return Response(serializer.data)

class InactiveTeacherDetailView(APIView):
    def get(self, request):
            # Retrieve the teacher based on emp_id, ensuring they are active
            teachers= models.Teacher.active.is_inactive()
            serializer=TeacherSerializer(teachers, many=True)
            return Response(serializer.data)