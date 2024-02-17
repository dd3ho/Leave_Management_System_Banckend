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
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        fname = self.request.query_params.get('fname')

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        if fname:
            queryset = queryset.filter(fname__icontains=fname)

        return queryset
