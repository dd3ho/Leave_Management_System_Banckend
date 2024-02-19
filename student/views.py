from rest_framework import viewsets
from .models import Student, StudentRegisterCourser
from .serializers import StudentSerializer, StudentRegisterCourserSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # GET /api/Students/
    # GET /Students/?user_id=12&fname=อุษา
    # GET /api/Students/?fname=อุษา
    # GET /api/Students/?user_id=12
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        fname = self.request.query_params.get('fname')

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        if fname:
            queryset = queryset.filter(fname__icontains=fname)

        return queryset


class StudentRegisterCourserViewSet(viewsets.ModelViewSet):
    queryset = StudentRegisterCourser.objects.all()
    serializer_class = StudentRegisterCourserSerializer
    
    # GET /studentRegister/
    # GET /studentRegister/?student_id=1&course_id=1
    # GET /studentRegister/?course_id=1
    # GET /studentRegister/?student_id=1
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('student_id')
        course_id = self.request.query_params.get('course_id')

        if student_id:
            queryset = queryset.filter(student_id=student_id)
            
        if course_id:
            queryset = queryset.filter(course_id=course_id)


        return queryset
