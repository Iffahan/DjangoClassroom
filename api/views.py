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
from django.core import serializers
from django.http import HttpResponse
from api.models import Assignment, AssignmentStatus
from .serializers import *



class ClassroomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Classroom.objects.all()

class AssignmentResultViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentResultSerializer
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return AssignmentResult.objects.all()

class ScoreViewSet(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Score.objects.all()


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

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Message.objects.all()



@api_view(['POST'])
def user_result_do(request,pk):
    data = request.data
    Result = data['result']
    Student = User.objects.get(username=request.user)
    Assignments = Assignment.objects.get(id=pk)
    assignmentStatus = AssignmentStatus.objects.create(assignment=Assignments, student = Student)
    assignmentStatus.status = Result
    assignmentStatus.save()
    
    studentScore = Score.objects.get(student = Student)


    AsResult = AssignmentResult.objects.get(assignment = Assignments)
    if Result == True:
        AsResult.TrueStudent.add(Student)
        studentScore.score = studentScore.score + 1

    else:
        AsResult.FalseStudent.add(Student)
    AsResult.save()
    studentScore.save()

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
def leave(request,pk):
    current_user = User.objects.get(username = request.user)
    classroom = Classroom.objects.get(id=pk)
    classroom.Member.remove(current_user)

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
def changeClass(request,pk):
    data = request.data
    ClassName = data['className']
    Teacher = data['teacher']
    ClassCode = data['classCode']
    teacher_user = User.objects.get(username=Teacher)
    classroom = Classroom.objects.get(id=pk)
    classroom.classroomName=ClassName
    classroom.teacher = teacher_user 
    classroom.classCode = ClassCode
    classroom.save()

    return Response({"change classroom success!"})

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
    assignments = Assignment.objects.create(classroom=classroomA, title = Title, description = Description, deadline=Deadline,choice_true=Choice_True,choice_false=Choice_False)
    assignments.save()
    assignmentResult = AssignmentResult.objects.create(assignment = assignments)

    return Response({"create assignment success!"})


@api_view(['POST'])
def changeAssignment(request,pk):
    data = request.data
    Title = data['title']
    Description = data['description']
    Deadline = data['deadline']
    Choice_True = data['choice_true']
    Choice_False = data['choice_false']
    assignment = Assignment.objects.get(id=pk)
    assignment.title = Title
    assignment.description = Description
    assignmentdeadline=Deadline
    assignment.choice_true=Choice_True
    assignment.choice_false=Choice_False
    assignment.save()

    return Response({"change assignment success!"})

@api_view(['GET'])
def getUserClassroom(request):
    nested_dict = {}
    n=0
    for item in Classroom.objects.filter(Member = request.user):
        nested_dict[n] = {"id" : item.id ,"name": item.classroomName}
        n = n + 1

    return JsonResponse(nested_dict)

@api_view(['GET'])
def getClassAssignment(request,pk):
    myassignment = {}
    n=0

    current_user = User.objects.get(username=request.user)
    for item in Assignment.objects.filter(id=pk):
        myassignment[n] = {'id': item.id, 'title': item.title}
        n= n+1

    return Response(myassignment)


@api_view(['POST'])
def postMessage(request,pk):
    data = request.data
    text_input = data['text']
    current_user = User.objects.get(username=request.user)
    classroom1 = Classroom.objects.get(id=pk)
    message = Message.objects.create(classroom=classroom1, user=current_user, text = text_input)
    message.save()

    return Response({"post":message.text})

@api_view(['POST'])
def changeMessage(request,pk):
    data = request.data
    text_input = data['text']
    current_user = User.objects.get(username=request.user)

    message = Message.objects.get(id=pk)
    message.text = text_input
    message.save()

    return Response({"change to":message.text})

@api_view(['POST'])
def deleteMessage(request,pk):

    message = Message.objects.get(id=pk)
    message.delete()

    return Response({"delete":message.text})

@api_view(['POST'])
def deleteClassroom(request,pk):

    classroom = Classroom.objects.get(id=pk)
    classroom.delete()

    return Response({"delete":classroom.classroomName})

@api_view(['POST'])
def deleteAssignment(request,pk):

    assignment = Assignment.objects.get(id=pk)
    assignment.delete()

    return Response({"delete":assignment.title})


@api_view(['GET'])
def getMessage(request,pk):
    classroom1 = Classroom.objects.get(id=pk)
    dic1 = {}
    n=0
    
    for item in Message.objects.filter(classroom=classroom1):
        dic1[n] = {'id': item.id, 'user':item.user.username, 'is_staff':item.user.is_staff, 'firstname':item.user.first_name, 'lastname':item.user.last_name, 'class': item.classroom.classroomName, 'text' : item.text }
        n= n+1

    return Response(dic1)

@api_view(['GET'])
def MyScore(request):
    dic = {}
    score = Score.objects.get(student=request.user)
    dic["score"] = score.score

    return Response(dic)

@api_view(['GET'])
def ClassMembers(request,pk):
    dic1 = {}
    n=0
    classroom1 = Classroom.objects.get(id=pk)
    Members = classroom1.Member.all()
    for item in Members:
        dic1[n] = {'id': item.id, 'user':item.username, 'firstname':item.first_name, 'lastname':item.last_name}
        n= n+1


    return Response(dic1)

@api_view(['GET'])
def AssignResult(request,pk):
    dic1 = {}
    dic2 = {}
    n=0

    assignments = Assignment.objects.get(id=pk)
    asResult = AssignmentResult.objects.get(assignment=assignments)
    trueStudent = asResult.TrueStudent.all()
    for item in trueStudent:
        dic1[n] = {'id': item.id, 'user':item.username, 'firstname':item.first_name, 'lastname':item.last_name}
        n= n+1

    m=0
    falseStudent = asResult.FalseStudent.all()
    for item in falseStudent:
        dic2[m] = {'id': item.id, 'user':item.username, 'firstname':item.first_name, 'lastname':item.last_name}
        m=m+1
    


    return Response({"TrueStudent":dic1, "FalseStudent":dic2})
