from rest_framework import viewsets
from education.models import Course, Faculty, Department
from .serializers import CourseSerializer, FacultySerializer, DepartmentSerializer


# Create your views here.
class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    # GET /education/department/
    # GET /education/department/?faculty_id=12&name=วิทยาการคอมพิวเตอร์
    # GET /education/department/?name=อุษา
    # GET /education/department/?faculty_id=12

    def get_queryset(self):
        queryset = super().get_queryset()
        faculty_id = self.request.query_params.get("faculty_id")
        name = self.request.query_params.get("name")

        if faculty_id:
            queryset = queryset.filter(faculty_id=faculty_id)

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
