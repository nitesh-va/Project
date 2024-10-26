from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from student import models
from django.db.models import Avg
from .serializers import StudentSerializer
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
           