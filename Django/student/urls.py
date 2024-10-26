from django.urls import path
from student.views import StudentViews

urlpatterns=[
    path('', StudentViews.as_view(),name="list_student"),
]