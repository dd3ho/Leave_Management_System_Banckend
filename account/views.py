from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # GET /api/users/
    # GET /api/users/?username=b6310451260&role=student
    # GET /api/users/?id=1
    # GET /api/users/?role=student
    
    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get("username")
        user_id = self.request.query_params.get("user_id")
        email = self.request.query_params.get("email")
        role = self.request.query_params.get("role")
        

        if username:
            queryset = queryset.filter(username__icontains=username)
        if user_id:
            queryset = queryset.filter(user_id__icontains=user_id)
        if email:
            queryset = queryset.filter(email__icontains=email)
        if role:
            queryset = queryset.filter(role__icontains=role)  
            
        return queryset
    
