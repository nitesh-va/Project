from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from department import models, serializers
from teacher import models as Teacher
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

class DepartmentActiveTeachersView(APIView):
    def get(self, request, dept_id):
        try:
            # Retrieve the department based on dept_id
            department = models.Department.active.get(dept_id=dept_id,is_active=True)
            # Get active teachers under this department
            active_teachers = models.Teacher.objects.filter(dept_name=department,is_active=True)

            # Prepare response data
            teachers_data = [
                {
                    'teacher_id': teacher.emp_id,
                    'name': teacher.name,
                    'is_active': teacher.is_active,
                }
                for teacher in active_teachers
            ]
            
            response_data = {
                'department_id': department.dept_id,
                'department_name': department.department_name,
                'active_teachers': teachers_data,
            }
            return Response(response_data, status=200)
        except models.Department.DoesNotExist:
            return Response({'error': 'Department not found or is not active.'}, status=404)

class DepartmentInactiveTeachersView(APIView):
    def get(self, request, dept_id):
        try:
            # Retrieve the department based on dept_id
            department =models.Department.active.is_active().get(dept_id=dept_id)
            # Get inactive teachers under this department
            inactive_teachers = models.Teacher.active.is_inactive()

            # Prepare response data
            teachers_data = [
                {
                    'teacher_id': teacher.emp_id,
                    'name': teacher.name,
                    'is_active': teacher.is_active,
                }
                for teacher in inactive_teachers
            ]
            
            response_data = {
                'department_id': department.dept_id,
                'department_name': department.department_name,
                'inactive_teachers': teachers_data,
            }
            return Response(response_data, status=200)
        except models.Department.DoesNotExist:
            return Response({'error': 'Department not found or is not active.'}, status=404)

class InactiveDepartment(APIView):
    def get(self, request):
            # Retrieve the data ensuring they are inactive
            departments= models.Department.active.is_inactive()
            serializer=serializers.DepartmentSerializer(departments, many=True)
            return Response(serializer.data)

class ActiveDepartment(APIView):
    def get(self, request):
            # Retrieve the data ensuring they are active
            departments= models.Department.active.is_active()
            serializer=serializers.DepartmentSerializer(departments, many=True)
            return Response(serializer.data)