from rest_framework import serializers, viewsets
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class ClassroomSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source = 'teacher.username', required = False, read_only = True)
    teacher_id = serializers.IntegerField(source = 'teacher.id', required = False, read_only = True)
    Member = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username") 
    
    class Meta:
        model = Classroom
        fields = '__all__'



# class StudentSerializer(serializers.ModelSerializer):
#     classroom = serializers.CharField(source = 'classroom.title', required = False, read_only = True)
#     classroom_id = serializers.IntegerField(source = 'classroom.id', required = False, read_only = True)
#     student_id = serializers.IntegerField(source = 'id', required = False, read_only = True)
#     class Meta:
#         model = Student
#         fields = ('student_id','classroom','classroom_id','students',)

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