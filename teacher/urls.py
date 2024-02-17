from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
