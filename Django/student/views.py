from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from student import models
from django.db.models import Avg

from .serializers import StudentSerializer

from .utils import cutoff_cleared,cutoff_notcleared
# Create your views here.

class StudentViews(APIView):
    def get(self,request):
        students=models.Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
 
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
class StudentByIdView(APIView):
    def get(self, request, roll_no):
            student = models.Student.objects.get(roll_no=roll_no)
            serializer = StudentSerializer(student)
            return Response(serializer.data)   

    def delete(self, request, roll_no):
            student = models.Student.objects.get(roll_no=roll_no)
            student.delete()  # Delete the student instance
            return Response(status=status.HTTP_204_NO_CONTENT)  # Return 204 No Content for successful deletion

    def put(self, request,roll_no):
        student=models.Student.objects.get(roll_no=roll_no)
        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TopperListView(APIView):
    def get(self, request):
        toppers = models.Student.objects.order_by('-percentage')[:2]  # Get the top 2 students based on percentage
        serializer = StudentSerializer(toppers, many=True)
        return Response(serializer.data)

class PassedStudents(APIView):
    def get(self, request):
         cut_percentage=40
         passed_students=cutoff_cleared(cut_percentage)
         serializer=StudentSerializer(passed_students,many=True)
         return Response(serializer.data)

class NotPassedStudents(APIView):
     def get(self,request):
        cut_percentage=40
        notpassed=cutoff_notcleared(cut_percentage)
        serializer=StudentSerializer(notpassed,many=True)
        return Response(serializer.data)

class Average(APIView):
    def get(self, request):
        averages = models.Student.objects.aggregate(
            average_total_marks=Avg('total_marks'),
            average_percentage=Avg('percentage')
        )
        return Response(averages)
    
class AverageMarksSubject(APIView):
    def get(self, request):
        averages = models.Student.objects.aggregate(
            maths=Avg('maths_marks'),
            physics=Avg('physics_marks'),
            chemistry=Avg('chemistry_marks')
        )
        return Response(averages) 