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
    
    
    # GET /education/course/
    # GET /education/course/?course_id=1&name=java
    # GET /education/course/?name=java
    # GET /education/course/?course_id=1

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        course_id = self.request.query_params.get("course_id")
        department_id = self.request.query_params.get("department_id")

        if course_id:
            queryset = queryset.filter(course_id=course_id)

        if name:
            queryset = queryset.filter(name__icontains=name)
        
        if department_id:
            queryset = queryset.filter(department_id=department_id)

        return queryset
