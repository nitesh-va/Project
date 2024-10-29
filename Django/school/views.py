from django.shortcuts import render



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from school import models
from .serializers import SchoolSerializer
from department.models import Department
# Create your views here.
class SchoolView(APIView):
    def get(self,request):
        schools=models.School.objects.all()
        serializer=SchoolSerializer(schools,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, school_id):
            school = models.School.objects.get(school_id=school_id)
            school.delete()  # Delete the student instance
            return Response(status=status.HTTP_204_NO_CONTENT)

class SchoolViewByID(APIView):
    def get(self, request, school_id):
            sch= models.School.objects.get(school_id=school_id)
            serializer = SchoolSerializer(sch)
            return Response(serializer.data)
    
    def put(self, request, school_id):
        sch = models.School.objects.get(school_id=school_id)
        serializer = SchoolSerializer(sch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InactiveSchool(APIView):
    def get(self, request):
            # Retrieve the teacher based on emp_id, ensuring they are active
            schools= models.School.active.is_inactive()
            serializer=SchoolSerializer(schools, many=True)
            return Response(serializer.data)


class ActiveSchool(APIView):
    def get(self, request):
            # Retrieve the teacher based on emp_id, ensuring they are active
            schools= models.School.active.is_active()
            serializer=SchoolSerializer(schools, many=True)
            return Response(serializer.data)


class SchoolActiveInactiveDepartment(APIView):
    def get(self, request, school_id):        
            # Retrieve the department based on dept_id
            #school =models.School.active.is_active().get(school_id=school_id)
            # Get inactive teachers under this department
        active_department = Department.active.is_active().filter(school__school_id=school_id,school__is_active=True).values()
        inactive_department = Department.active.is_inactive().filter(school__school_id=school_id,school__is_active = True).values()
        respone_data = {'active_department': active_department, 'inactive_department': inactive_department}
        return Response(respone_data, status=200)
        
