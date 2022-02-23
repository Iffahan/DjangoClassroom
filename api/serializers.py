from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ClassroomSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source = 'teacher.username', required = False, read_only = True)
    teacher_id = serializers.IntegerField(source = 'teacher.id', required = False, read_only = True)
    class Meta:
        model = Classroom
        fields = ('id', 'title','teacher', 'teacher_id')