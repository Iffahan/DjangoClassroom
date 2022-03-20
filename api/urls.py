from django.db import router
from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
# router.register(r'students', StudentViewSet, basename='student')
router.register(r'classroom', ClassroomViewSet, basename='classroom')
router.register(r'assignments', AssignmentViewSet, basename='assignment')
router.register(r'assignment_status', AssignmentStatusViewSet, basename='assignment_status')

urlpatterns = [
    path(r'', include(router.urls)),
    path('user_result_do/<int:pk>', views.user_result_do),
    path('userdetail', views.UserDetail),
    path('addUser/<int:pk>', views.addUser),
    path('removeUser/<int:pk>', views.removeUser),
    path('createClass', views.createClass),
    path('join', views.join),
    path('myclass', views.myclass),
    path('changeProfile', views.changeProfile),
    path('changeEmail', views.changeEmail),
    path('createAssignment/<int:pk>', views.createAssignment),

]