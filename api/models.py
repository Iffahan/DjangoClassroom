from django.db import models
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Classroom(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Student(models.Model):
    students = models.ManyToManyField(User, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.classroom.title

class Assignment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(default=datetime.now, blank=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null = True)
    
    UNGRADED = 0
    POOR = 1
    BELOW_AVERAGE = 2
    AVERAGE = 3
    GOOD = 4
    EXCELLENT = 5

    SCORE_CHOICES = (
        (UNGRADED, 'Ungraded'),
        (str(POOR), ('1 - Very Poor')),
        (str(BELOW_AVERAGE), ('2 - Below Average')),
        (str(AVERAGE), ('3 - Average')),
        (str(GOOD), ('4 - Good')),
        (str(EXCELLENT), ('5 - Excellent'))
    )

    score = models.BooleanField(choices=SCORE_CHOICES, default=False)

    def __str__(self):
        return self.title

class AssignmentStatus(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null = True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    
    BOOL_CHOICES = ((True, 'Completed'), (False, 'Incomplete'))

    status = models.BooleanField(choices=BOOL_CHOICES, default=False)

    def __str__(self):
        return self.student.username
