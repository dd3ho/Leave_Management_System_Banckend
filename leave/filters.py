import django_filters
from .models import LeaveRequestDetail

class LeaveRequestDetailFilter(django_filters.FilterSet):
    section = django_filters.CharFilter(field_name='course_id__section', lookup_expr='exact')
    teacher_id = django_filters.NumberFilter(field_name='teacher_id', lookup_expr='exact')
    course_name = django_filters.CharFilter(field_name='course_id__name', lookup_expr='icontains')

    class Meta:
        model = LeaveRequestDetail
        fields = ['section', 'teacher_id', 'course_name']
