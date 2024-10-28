from django.urls import path
from .views import SchoolView,SchoolViewByID,ActiveSchool,InactiveSchool

urlpatterns = [
    path('',SchoolView.as_view(),name='school'),
    path('<int:school_id>/', SchoolView.as_view(),name='school_ID'),
    path('school/<int:school_id>/', SchoolViewByID.as_view(), name='school_ID'),
    path('active/', ActiveSchool.as_view(), name='active_school'),
    path('inactive/', InactiveSchool.as_view(), name='inactive_school'),
]