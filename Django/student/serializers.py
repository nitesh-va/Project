from rest_framework import serializers
from student import models


class StudentSerializer(serializers.ModelSerializer):
    # emp_id=TeacherSerializer(read_only=True)
    class Meta:
        model = models.Student
        fields = '__all__'

