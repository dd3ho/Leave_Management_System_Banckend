from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, InstructorCourseViewSet

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'instructorCourse', InstructorCourseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
