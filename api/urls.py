from django.db import router
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'classroom', ClassroomViewSet, basename='classroom')

urlpatterns = [
    path(r'', include(router.urls)),
]