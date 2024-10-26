from django.urls import path
from student.views import StudentViews,StudentByIdView

urlpatterns=[
    path('', StudentViews.as_view(),name="list_student"),
    path('students/<int:roll_no>/', StudentByIdView.as_view(), name='student_by_roll_no'), 
]  