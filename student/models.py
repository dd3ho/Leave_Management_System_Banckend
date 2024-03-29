from django.db import models
from account.models import User
from education.models import Course, Faculty, Department

# Create your models here.
class Student(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    prefix = models.CharField(max_length=20, blank=True, null=True)
    fname = models.CharField(
        max_length=255)
    lname = models.CharField(
        max_length=255)
    faculty_id = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, blank=True)
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE,null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)

class StudentRegisterCourser(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
