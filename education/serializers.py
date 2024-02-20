from rest_framework import serializers
from .models import  Course, Faculty, Department
from django.utils.translation import gettext_lazy as _



class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
        dept = 2
        
        
class DepartmentSerializer(serializers.ModelSerializer):
    faculty_id = serializers.PrimaryKeyRelatedField(
        queryset=Faculty.objects.all(),
        required=True
    )
    default_error_messages = {
        'department_already_exists': _(
            'This Department already exists.'
        )
    }
    class Meta:
        model = Department
        fields = '__all__'
        depth = 2
        
    def validate(self, attrs):
        if Department.objects.filter(
                faculty_id=attrs.get('faculty_id')).filter(
                name=attrs.get(
                    'name')).exists():
            raise serializers.ValidationError({
                'name': self.error_messages['department_already_exists']
            })
        return attrs
    
    def save(self):
        data = self._validated_data
        department = self.Meta.model(**data)
        department.save()

        return DepartmentSerializer(department).data


class CourseSerializer(serializers.ModelSerializer):
    faculty_id = serializers.PrimaryKeyRelatedField(
        queryset=Faculty.objects.all(),
        required=True
    )
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        required=True
    )
    class Meta:
        model = Course
        fields = '__all__'
        depth = 2
        
