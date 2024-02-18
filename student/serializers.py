from rest_framework import serializers
from .models import  Student
from account.models import User
from django.utils.translation import gettext_lazy as _



class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True
    )
    class Meta:
        model = Student
        fields = '__all__'
        dept = 2
        
