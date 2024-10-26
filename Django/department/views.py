from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from department import models, serializers
# Create your views here.


class DepartmentView(APIView):
    def get(self,request):
        departments=models.Department.objects.all()
        serializer=serializers.DepartmentSerializer(departments,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=serializers.DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, dept_id):
            dept = models.Department.objects.get(dept_id=dept_id)
            dept.delete()  # Delete the student instance
            return Response(status=status.HTTP_204_NO_CONTENT) 

class DepartmentViewByID(APIView):
    def get(self, request, dept_id):
            dept= models.Department.objects.get(dept_id=dept_id)
            serializer = serializers.DepartmentSerializer(dept)
            return Response(serializer.data)
    
    def put(self, request, dept_id):
        dept = models.Department.objects.get(dept_id=dept_id)
        serializer = serializers.DepartmentSerializer(dept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    