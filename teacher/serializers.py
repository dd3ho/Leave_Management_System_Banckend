from rest_framework import serializers
from .models import  Teacher, InstructorCourse
from account.models import User
from education.models import Course
from education.serializers import CourseSerializer
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
    teacher_data = TeacherSerializer(source='teacher_id', read_only=True)
    # teacher_id = serializers.IntegerField(source='teacher_id.id', read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        required=True
    )
    course_data = CourseSerializer(source='course_id', read_only=True)
    class Meta:
        model = InstructorCourse
        fields = '__all__'
        depth = 2
        
