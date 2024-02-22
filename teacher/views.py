from rest_framework import viewsets
from .models import Teacher, InstructorCourse
from .serializers import TeacherSerializer, InstructorCourseSerializer

# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    # GET /teacher/
    # GET /teacher/?user_id=12&fname=อุษา
    # GET /teacher/?fname=อุษา
    # GET /teacher/?user_id=12
    # GET /teacher/?faculty_id=วิทยาศาสตร์&department_id=วิทยาการคอมพิวเตอร์
    # GET /teacher/?faculty_id=วิทยาศาสตร์
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        faculty_id = self.request.query_params.get('faculty_id')
        department_id = self.request.query_params.get('department_id')
        fname = self.request.query_params.get('fname')

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        if fname:
            queryset = queryset.filter(fname__icontains=fname)

        if faculty_id:
            queryset = queryset.filter(faculty_id=faculty_id)
        
        if department_id:
            queryset = queryset.filter(department_id=department_id)
            
        return queryset


class InstructorCourseViewSet(viewsets.ModelViewSet):
    queryset = InstructorCourse.objects.all()
    serializer_class = InstructorCourseSerializer
    
    # GET /instructorCourse/
    # GET /instructorCourse/?teacher_id=1&course_id=2
    # GET /instructorCourse/?course_id=2
    # GET /instructorCourse/?teacher_id=1
    # GET /instructorCourse/?teacher_id=1&course_id=2
    # GET /instructorCourse/?teacher_id=1
    

    def get_queryset(self):
        queryset = super().get_queryset()
        teacher_id = self.request.query_params.get('teacher_id')
        course_id = self.request.query_params.get('course_id')

        if teacher_id:
            queryset = queryset.filter(teacher_id=teacher_id)
        if course_id:
            queryset = queryset.filter(course_id=course_id)

        return queryset
