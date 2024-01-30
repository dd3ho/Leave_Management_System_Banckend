from django.db import models
from account.models import User
from teacher.models import Teacher
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
