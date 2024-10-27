from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TeacherSerializer

from teacher import models

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
            teacher.delete()  # Delete the student instance
            return Response(status=status.HTTP_204_NO_CONTENT)
    
class TeacherPerformance(APIView):
    def get(self, request):
        return Response(get_teacher_performance())