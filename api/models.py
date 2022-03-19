from enum import unique
import re
from django.db import models
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User,Group
from django.utils.crypto import get_random_string



class Classroom(models.Model):
    classroomName = models.CharField(max_length=30, default='Classroom Name')
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher')
    Member = models.ManyToManyField(User,related_name='member')
    def __str__(self):
        return self.classroomName

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    posted_date = models.DateTimeField(default=datetime.now, blank=True)
    deadline = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.title

class AssignmentStatus(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null = True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    
    BOOL_CHOICES = ((True, 'Completed'), (False, 'Incomplete'))

    status = models.BooleanField(choices=BOOL_CHOICES, default=False)

    def __str__(self):
        return self.student.username




