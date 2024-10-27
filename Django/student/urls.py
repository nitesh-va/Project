from django.urls import path
from student.views import StudentViews,StudentByIdView,TopperListView,PassedStudents,NotPassedStudents
from student.views import Average,AverageMarksSubject
urlpatterns=[
    path('', StudentViews.as_view(),name="list_student"),
    path('<int:roll_no>/', StudentByIdView.as_view(), name='student_by_roll_no'), 
    path('topper/',TopperListView.as_view(),name='topper_list'),
    path('passed/', PassedStudents.as_view(), name='not_passed_list'),
    path('not_passed/', NotPassedStudents.as_view(), name='not_passed_list'),
    path('average/', Average.as_view(), name='average_marks'),
    path('average/subject/', AverageMarksSubject.as_view(), name='average_marks_subject'),
]

