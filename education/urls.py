from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, DepartmentViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'faculty', FacultyViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'course', CourseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
