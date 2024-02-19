from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, StudentRegisterCourserViewSet

router = DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'studentRegister', StudentRegisterCourserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
