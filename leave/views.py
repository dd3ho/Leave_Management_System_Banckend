from rest_framework import viewsets
from .models import Files
from .serializer import FileSerializer


class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer
