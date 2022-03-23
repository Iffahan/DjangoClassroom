from rest_framework import serializers, viewsets
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Value as V
from django.db.models.functions import Concat   


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class ClassroomSerializer(serializers.ModelSerializer):
    teacher_firstname = serializers.CharField(source = 'teacher.first_name' , required = False, read_only = True)
    teacher_lastname = serializers.CharField(source = 'teacher.last_name', required = False, read_only = True)
    teacher_id = serializers.IntegerField(source = 'teacher.id', required = False, read_only = True)
    Member = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field='first_name') 
    
    class Meta:
        model = Classroom
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source = 'teacher.username', required = False, read_only = True)
    assignment_id = serializers.IntegerField(source = 'assignment.id', required = False, read_only = True)
    classroom = serializers.CharField(source = 'classroom.title', required = False, read_only = True)
    classroom_id = serializers.IntegerField(source = 'classroom.id', required = False, read_only = True)
    class Meta:
        model = Assignment
        fields = '__all__'

class AssignmentStatusSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source = 'student.username', required = False, read_only = True)
    student_id = serializers.IntegerField(source = 'student.id', required = False, read_only = True)
    assignment = serializers.CharField(source = 'assignment.title', required = False, read_only = True)
    assignment_id = serializers.IntegerField(source = 'assignment.id', required = False, read_only = True)
    class Meta:
        model = AssignmentStatus
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):  
    classroom = serializers.CharField(source = 'classroom.title', required = False, read_only = True)
    user = serializers.CharField(source = 'user.username', required = False, read_only = True)
    user_firtname = serializers.CharField(source = 'user.firts_name', required = False, read_only = True)
    user_last_name = serializers.CharField(source = 'user.lastname', required = False, read_only = True)
    class Meta:
        model = Message
        fields = '__all__'