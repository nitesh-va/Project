from django.urls import path
from .views import UserView,LoginView

urlpatterns = [
     path('',UserView.as_view(),name='all'),
     path('login/', LoginView.as_view(), name='login'),
 ]