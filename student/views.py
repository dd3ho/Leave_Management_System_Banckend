from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

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
