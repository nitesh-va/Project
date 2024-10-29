from django.urls import path
from .views import SchoolView,SchoolViewByID,ActiveSchool,InactiveSchool,SchoolActiveInactiveDepartment

urlpatterns = [
    path('',SchoolView.as_view(),name='school'),
    path('<int:school_id>/', SchoolView.as_view(),name='school_ID'),
    path('school/<int:school_id>/', SchoolViewByID.as_view(), name='school_ID'),
    path('active/', ActiveSchool.as_view(), name='active_school'),
    path('inactive/', InactiveSchool.as_view(), name='inactive_school'),
    path('active_inactive/<int:school_id>/', SchoolActiveInactiveDepartment.as_view(), name='active_department')  
]