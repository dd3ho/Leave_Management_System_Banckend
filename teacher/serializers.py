from rest_framework import serializers
from .models import  Teacher
from account.models import User
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
        
