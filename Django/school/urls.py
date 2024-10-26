from django.urls import path
from .views import SchoolView,SchoolViewByID

urlpatterns = [
    path('',SchoolView.as_view(),name='school'),
    path('<int:school_id>/', SchoolView.as_view(),name='school_ID'),
    path('school/<int:school_id>/', SchoolViewByID.as_view(), name='school_ID'),
]