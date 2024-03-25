from rest_framework import serializers
from .models import Files, LeaveRequest, LeaveRequestDetail
from django.utils.translation import gettext_lazy as _
from education.models import Course
from education.serializers import CourseSerializer
from .models import Student
from student.serializers import StudentSerializer
from .models import Teacher
from teacher.serializers import TeacherSerializer



class LeaveRequestSerializer(serializers.ModelSerializer):
    file_id = serializers.FileField(required=False)

    class Meta:
        model = LeaveRequest
        fields = "__all__"
        dept = 2

    def validate_file_id(self, attrs):
        if not attrs.content_type == "application/pdf":
            raise serializers.ValidationError("Only PDF files are allowed.")
        return attrs

    def save(self):
        data = self._validated_data
        leaveRequest = self.Meta.model(**data)
        leaveRequest.save()
        print("Saved LeaveRequest")
        print(leaveRequest.id)

        return leaveRequest


class LeaveRequestDetailSerializer(serializers.ModelSerializer):
    leave_request_id = serializers.PrimaryKeyRelatedField(
        queryset=LeaveRequest.objects.all(), required=False
    )
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), required=False
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), required=False
    )
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), required=False
    )

    leave_request_data = LeaveRequestSerializer(
        source="leave_request_id", read_only=False, required=False
    )
    approve_id_by = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        required=False,  # Add this line to make the field optional
        allow_null=True  # Add this line to allow null values
    )
    teacher_data = TeacherSerializer(source="teacher_id", read_only=True)
    student_data = StudentSerializer(source="student_id", read_only=True)
    course_data = CourseSerializer(source="course_id", read_only=True)
    approve_id_by_data = TeacherSerializer(source="approve_id_by",read_only=True)

    class Meta:
        model = LeaveRequestDetail
        fields = "__all__"
        dept = 2


class FileSerializer(serializers.ModelSerializer):
    leave_request_id = serializers.PrimaryKeyRelatedField(
        queryset=LeaveRequest.objects.all(), required=False
    )
    
    class Meta:
        model = Files
        fields = "__all__"
        dept = 2
