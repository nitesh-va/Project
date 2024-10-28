from django.urls import path
from student.views import StudentViews,StudentByIdView,TopperListView,PassedStudents,NotPassedStudents
from student.views import Average,AverageMarksSubject,InactiveStudent,ActiveStudent
urlpatterns=[
    path('', StudentViews.as_view(),name="list_student"),
    path('<int:roll_no>/', StudentByIdView.as_view(), name='student_by_roll_no'), 
    path('topper/',TopperListView.as_view(),name='topper_list'),
    path('passed/', PassedStudents.as_view(), name='not_passed_list'),
    path('not_passed/', NotPassedStudents.as_view(), name='not_passed_list'),
    path('average/', Average.as_view(), name='average_marks'),
    path('average/subject/', AverageMarksSubject.as_view(), name='average_marks_subject'),
    path('inactive/', InactiveStudent.as_view(), name='inactive_student'),
    path('active/', ActiveStudent.as_view(), name='active_student')
]

