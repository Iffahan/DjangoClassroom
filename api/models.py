from django.db import models
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Classroom(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

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
    user_code = models.CharField(max_length=200, null = True)
    
    BOOL_CHOICES = ((True, 'Completed'), (False, 'Incomplete'))

    status = models.BooleanField(choices=BOOL_CHOICES, default=False)

    def __str__(self):
        return self.student.username


