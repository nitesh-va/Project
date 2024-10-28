from django.urls import path
from .views import DepartmentView,DepartmentViewByID,DepartmentInactiveTeachersView
from .views import DepartmentActiveTeachersView,ActiveDepartment,InactiveDepartment

urlpatterns = [
    path('', DepartmentView.as_view(), name='department_list'),
    path('<int:dept_id>/', DepartmentView.as_view(), name='department_detail'),
    path('dept/<int:dept_id>/', DepartmentViewByID.as_view(), name='department_detail'),
    path('<int:dept_id>/inactive_teacher/', DepartmentInactiveTeachersView.as_view(), name='department_inactive_teachers'),
    path('<int:dept_id>/active_teacher/', DepartmentActiveTeachersView.as_view(), name='department_active_teachers'),
    path('active/', ActiveDepartment.as_view(), name='active_department'),
    path('inactive/', InactiveDepartment.as_view(), name='inactive_department'),
    
]
