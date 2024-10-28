from django.urls import path
from .views import TeacherViews,TeacherByIdView,TeacherPerformance,PassedFailedStudentsCountView,TeacherActiveStudentsView
from .views import TeacherNotActiveStudentsView,ActiveTeacherDetailView,InactiveTeacherDetailView
urlpatterns=[
    path('', TeacherViews.as_view(), name='teacher_list'),
    path('<int:emp_id>/', TeacherByIdView.as_view(), name='teacher_detail'),
    path('performance/', TeacherPerformance.as_view(), name='teacher_performance'),
    path('passed-failed-count/', PassedFailedStudentsCountView.as_view(), name='passed_failed_count'),
    path('<int:emp_id>/active/', TeacherActiveStudentsView.as_view(), name='teacher_active_students'),
    path('<int:emp_id>/notactive/', TeacherNotActiveStudentsView.as_view(), name='teacher_notactive_students'),
    path('active/', ActiveTeacherDetailView.as_view(), name='active_teacher_detail'),
    path('inactive/', InactiveTeacherDetailView.as_view(), name='inactive_teacher_detail'),
]
