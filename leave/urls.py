from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilesViewSet, LeaveRequestViewSet, LeaveRequestDetailViewSet

router = DefaultRouter()
router.register("files", FilesViewSet, basename="files")
router.register("leaveRequest", LeaveRequestViewSet)
router.register("leaveDetail", LeaveRequestDetailViewSet)

urlpatterns = [path("", include(router.urls))]
