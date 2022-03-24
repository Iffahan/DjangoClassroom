from django.db import router
from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'classroom', ClassroomViewSet, basename='classroom')
router.register(r'assignments', AssignmentViewSet, basename='assignment')
router.register(r'assignment_status', AssignmentStatusViewSet, basename='assignment_status')
router.register(r'message', MessageViewSet, basename='message')
router.register(r'score', ScoreViewSet, basename='score')

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
    path('getUserClassroom', views.getUserClassroom),
    path('getClassAssignment/<int:pk>', views.getClassAssignment),
    path('postMessage/<int:pk>', views.postMessage),
    path('changeMessage/<int:pk>', views.changeMessage),
    path('deleteMessage/<int:pk>', views.deleteMessage),
    path('deleteClassroom/<int:pk>', views.deleteClassroom),
    path('getMessage/<int:pk>', views.getMessage),
    path('leave/<int:pk>', views.leave),

]