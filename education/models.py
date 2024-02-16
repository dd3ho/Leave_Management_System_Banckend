from django.db import models
from account.models import User

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=255)

class Department(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
     


class Course(models.Model):
    name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=20)
    faculty_id = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, blank=True)
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE,null=True, blank=True)
    section = models.CharField(max_length=10)
