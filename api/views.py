from hashlib import new
from pydoc import classname
from django.shortcuts import render
from django.db.models import query
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.generics import *
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.http import Http404, HttpResponseNotFound  
from django.db.models import fields
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
from django_filters.filters import DateTimeFilter
from rest_framework import generics, viewsets, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.fields import datetime
from rest_framework.response import Response
from rest_framework import permissions
from django.http import JsonResponse

from api.models import Assignment, AssignmentStatus
from .serializers import *



class ClassroomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Classroom.objects.all()


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Assignment.objects.all()

class AssignmentStatusViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentStatusSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return AssignmentStatus.objects.all()


@api_view(['POST'])
def user_result_do(request,pk):
    data = request.data
    Result = data['result']
    Student = User.objects.get(username=request.user)
    Assignments = Assignment.objects.get(id=pk)
    assignmentStatus = AssignmentStatus.objects.create(assignment=Assignments, student = Student)
    assignmentStatus.status = Result
    assignmentStatus.save()

    return Response({"success!"})


@api_view(['GET'])
def UserDetail(request):
    s = UserSerializer(request.user)
    return Response(s.data)

@api_view(['POST'])
def addUser(request,pk):
    data = request.data
    Email = data['email']
    newuser = User.objects.get(email=Email)
    classroom = Classroom.objects.get(id=pk)
    classroom.Member.add(newuser)

    return Response({"success"})

@api_view(['POST'])
def removeUser(request,pk):
    data = request.data
    Email = data['email']
    newuser = User.objects.get(email=Email)
    classroom = Classroom.objects.get(id=pk)
    classroom.Member.remove(newuser)

    return Response({"success"})

@api_view(['POST'])
def createClass(request):
    data = request.data
    ClassName = data['className']
    Teacher = data['teacher']
    ClassCode = data['classCode']
    teacher_user = User.objects.get(username=Teacher)
    classroom = Classroom.objects.create(classroomName=ClassName, teacher = teacher_user, classCode = ClassCode)
    classroom.save()

    return Response({"create classroom success!"})

@api_view(['POST'])
def join(request):
    data = request.data
    ClassCode = data['classCode']
    newuser = User.objects.get(username=request.user)
    classroom = Classroom.objects.get(classCode = ClassCode)
    classroom.Member.add(newuser)

    return Response("success! you join the class")

@api_view(['GET'])
def myclass(request):
    current_user = User.objects.get(username=request.user)
    classroom = Classroom.objects.filter(Member = current_user)

    return Response(classroom)

@api_view(['POST'])
def changeProfile(request):
    data = request.data
    FIRSTNAME = data['first_name']
    LASTNAME = data['last_name']
    current_user = User.objects.get(username=request.user)
    current_user.first_name = FIRSTNAME
    current_user.last_name = LASTNAME
    current_user.save()

    return Response({"change to" :[current_user.first_name,current_user.last_name]})

@api_view(['POST'])
def changeEmail(request):
    data = request.data
    Email = data['email']
    current_user = User.objects.get(username=request.user)
    current_user.email = Email
    current_user.save()

    return Response({"change to" :[current_user.email]})

@api_view(['POST'])
def createAssignment(request,pk):
    data = request.data
    Title = data['title']
    Description = data['description']
    Deadline = data['deadline']
    Choice_True = data['choice_true']
    Choice_False = data['choice_false']
    classroomA = Classroom.objects.get(id=pk)
    assignment = Assignment.objects.create(classroom=classroomA, title = Title, description = Description, deadline=Deadline,choice_true=Choice_True,choice_false=Choice_False)
    assignment.save()

    return Response({"create assignment success!"})

@api_view(['GET'])
def getUserClassroom(request):
    current_user = User.objects.get(username=request.user)
    
    return Response({"classroom" :[item.classroomName for item in Classroom.objects.filter(Member=current_user)]})
