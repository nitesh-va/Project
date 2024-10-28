from django.urls import path
from .views import TeacherViews,TeacherByIdView,TeacherPerformance,PassedFailedStudentsCountView

urlpatterns=[
    path('', TeacherViews.as_view(), name='teacher_list'),
    path('<int:emp_id>/', TeacherByIdView.as_view(), name='teacher_detail'),
    path('performance/', TeacherPerformance.as_view(), name='teacher_performance'),
    path('passed-failed-count/', PassedFailedStudentsCountView.as_view(), name='passed_failed_count'),
    
]
