from rest_framework import serializers
from .models import  Teacher, InstructorCourse
from account.models import User
from education.models import Course
from django.utils.translation import gettext_lazy as _



class TeacherSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True
    )
    class Meta:
        model = Teacher
        fields = '__all__'
        dept = 2


class InstructorCourseSerializer(serializers.ModelSerializer):
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        required=True
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        required=True
    )
    class Meta:
        model = InstructorCourse
        fields = '__all__'
        dept = 2
        
