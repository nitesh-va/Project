# Day 1

##  Django API for CRUD Operations

### Introduction

This guide provides a step-by-step process to build a Django project that enables CRUD (Create, Read, Update, Delete) functionalities using the Django REST Framework (DRF) and Postman for API testing.

#### What is Django REST Framework?

Django REST Framework (DRF) is a robust toolkit designed for developing RESTful APIs with Django. It streamlines the API creation process and includes features such as:

- **Serialization**: Converts complex data types into Python data structures suitable for API responses.
- **Authentication and Permissions**: Implements built-in authentication options to secure APIs.
- **Browsable API**: Offers a user-friendly web interface for developers to interact with APIs during development.

### Serializers in DRF

In DRF, serializers play a crucial role in transforming Django model instances into native Python types, which can then be rendered into formats like JSON.

#### Key Functions of Serializers:

1. **Serialization**: Converts model instances or querysets to JSON for API output.
2. **Deserialization**: Processes incoming JSON data and translates it back into Python objects or Django models.
3. **Validation**: Ensures incoming data adheres to defined formats before it is stored in the database.

#### Sample Serializer Code:

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_no']
```
# Setting Up URL Patterns

In Django Rest framework, URL patterns dictate the API endpoints, linking specific URL paths to views that handle CRUD operations.

### Example URL Configuration:
```python
from django.urls import path
from .views import StudentListCreateView, StudentDetailView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),  # Retrieve all students, Create
    path('students/<int:roll_no>/', StudentDetailView.as_view(), name='student-detail'),  # Retrieve, Update, Delete by ID
]
```
# Student Management API

This project implements an API to manage student information, including the following operations:

* Retrieve all students
* Retrieve a student by ID
* Create a new student
* Update a student by ID
* Delete a student by ID

### Defining the Student Model
The model for storing student data is defined as follows:
```python 
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name
```
# Implementing Views

The views contain the logic for handling CRUD operations using Data Rest Framework's generic views for efficiency.

#### 1. Retrieve All Students
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
```
#### 2. Retrieve a Student by ID
```python
class StudentDetailView(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
```
#### 3. Create a New Student
```python
class StudentListCreateView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```
#### 4. Update a Student by ID
```python
class StudentDetailView(APIView):
    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
```
#### 5. Delete a Student by ID
```python
class StudentDetailView(APIView):
    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response({'message': 'Student deleted successfully'}, status=200)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
```
# Testing the API with Postman
Once the API is set up, you can test each endpoint using Postman by configuring requests for different operations—GET, POST, PUT, and DELETE—and inspecting the responses.

This approach allows for effective management of student data through Django and Django Rest Framework, providing a solid foundation for further enhancements.

# Day 2
# Django Student Management API

## Overview

The Student Management API is designed using Django and the Django REST Framework (DRF). This API offers various endpoints for managing student records, calculating performance metrics, and retrieving specific data.

## Models

### Student_Task Model

The `Student_Task` model stores data related to students and includes the following fields:

1. **name**:
   - **Type**: CharField
   - **Max Length**: 50
   - **Description**: Holds the name of the student.

2. **roll_no**:
   - **Type**: IntegerField
   - **Default**: 0
   - **Primary Key**: Yes
   - **Description**: Serves as a unique identifier for each student.

3. **chemistry**:
   - **Type**: IntegerField
   - **Default**: 0
   - **Description**: Represents the marks obtained in Chemistry.

4. **physics**:
   - **Type**: IntegerField
   - **Default**: 0
   - **Description**: Represents the marks obtained in Physics.

5. **maths**:
   - **Type**: IntegerField
   - **Default**: 0
   - **Description**: Represents the marks obtained in Maths.

6. **class_teacher**:
   - **Type**: CharField
   - **Max Length**: 50
   - **Description**: Represents the name of the student's class teacher.

### Methods

- **total_marks()**: 
  - **Description**: Calculates the total marks obtained by the student across all subjects (Chemistry, Physics, Maths).
  
- **percentage()**: 
  - **Description**: Computes the percentage of marks obtained based on the total marks.

- **__str__()**: 
  - **Description**: Returns the name of the student as the string representation of the model instance.

## API Endpoints

### 1. Student Management

- **Add Student**
  - **URL**: `/add/`
  - **Method**: `POST`
  - **Description**: Create a new student record.

- **List Students**
  - **URL**: `/list/`
  - **Method**: `GET`
  - **Description**: Retrieve all student records.

- **Update Student**
  - **URL**: `/update/<int:roll_no>/`
  - **Method**: `PUT`
  - **Description**: Update an existing student record.

- **Delete Student**
  - **URL**: `/delete/<int:roll_no>/`
  - **Method**: `DELETE`
  - **Description**: Delete an existing student record.

---

### 2. Performance Analysis

- **Get Toppers**
  - **URL**: `/toppers/`
  - **Method**: `GET`
  - **Description**: Retrieve the top 5 students based on total marks.

- **Students Above Cutoff**
  - **URL**: `/cutoff/`
  - **Method**: `GET`
  - **Description**: Retrieve students who scored 150 or more total marks.

- **Failed Students**
  - **URL**: `/failed/`
  - **Method**: `GET`
  - **Description**: Retrieve students who have failed in one or more subjects.

- **Students by Average Marks**
  - **URL**: `/avg/`
  - **Method**: `GET`
  - **Description**: Retrieve students who scored above or below the average.

- **Subject-Wise Failed Students**
  - **URL**: `/subject_failed/`
  - **Method**: `GET`
  - **Description**: Retrieve students who failed in specific subjects.

- **Students by Class Teacher**
  - **URL**: `/teacher/`
  - **Method**: `GET`
  - **Description**: Retrieve students grouped by their class teacher.

- **Performance of Teachers**
  - **URL**: `/performance/`
  - **Method**: `GET`
  - **Description**: Retrieve performance metrics of teachers based on their students' results.

## Serializers

The `StudentTaskSerializer` is utilized for serializing the `Student_Task` model data:

```python
from rest_framework import serializers
from .models import Student_Task

class StudentTaskSerializer(serializers.ModelSerializer):
    total_marks = serializers.SerializerMethodField()
    percentage = serializers.SerializerMethodField()

    class Meta:
        model = Student_Task
        fields = ['name', 'roll_no', 'chemistry', 'physics', 'maths', 'class_teacher', 'total_marks', 'percentage']

    def get_total_marks(self, obj):
        return obj.total_marks()

    def get_percentage(self, obj):
        return obj.percentage()
```
## Admin Registration
```python 
from django.contrib import admin
from student.models import Student
from unfold.admin import ModelAdmin as UnfoldModelAdmin
# Register your models here.
class StudentAdmin(UnfoldModelAdmin):
    list_display = ['name', 'roll_no', 'maths_marks','physics_marks','chemistry_marks','total_marks','percentage','emp_id','dept_name']


admin.site.register(Student,StudentAdmin)
```
