from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'faculty', FacultyViewSet)
router.register(r'department', DepartmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
