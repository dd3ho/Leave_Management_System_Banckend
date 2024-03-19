from rest_framework import serializers
from .models import  Student, StudentRegisterCourser
from account.models import User
from django.utils.translation import gettext_lazy as _
from education.models import Course
from education.serializers import CourseSerializer
from account.serializers import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True
    )
    user_data = UserSerializer(source='user_id', read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        dept = 2
        
class StudentRegisterCourserSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(),
        required=True
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        required=True
    )
    student_data = StudentSerializer(source='student_id', read_only=True)
    course_data = CourseSerializer(source='course_id', read_only=True)
    default_error_messages = {
        'studentRegisterCourser_already_exists': _(
            'This StudentRegisterCourser already exists.'
        )
    }
    class Meta:
        model = StudentRegisterCourser
        fields = '__all__'
        dept = 2

    def validate(self, attrs):
            if StudentRegisterCourser.objects.filter(
                    student_id=attrs.get('student_id')).filter(
                    course_id=attrs.get(
                        'course_id')).exists():
                raise serializers.ValidationError({
                    'student_id': self.error_messages['studentRegisterCourser_already_exists']
                })
            
            return attrs

    def save(self):
        data = self._validated_data
        studentRegisterCourser = self.Meta.model(**data)
        studentRegisterCourser.save()

        return StudentRegisterCourserSerializer(studentRegisterCourser).data   
