from django.urls import path
from .views import TeacherViews,TeacherByIdView

urlpatterns=[
    path('', TeacherViews.as_view(), name='teacher_list'),
    path('<int:emp_id>/', TeacherByIdView.as_view(), name='teacher_detail'),
    
]
