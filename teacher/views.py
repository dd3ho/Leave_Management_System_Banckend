from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer

# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    # GET /api/teachers/
    # GET /teachers/?user_id=12&fname=อุษา
    # GET /api/teachers/?fname=อุษา
    # GET /api/teachers/?user_id=12
    # GET /teachers/?faculty_id=วิทยาศาสตร์&department_id=วิทยาการคอมพิวเตอร์
    # GET /teachers/?faculty_id=วิทยาศาสตร์
    
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
