from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilesViewSet, LeaveRequestViewSet, LeaveRequestDetailViewSet

router = DefaultRouter()
router.register("files", FilesViewSet, basename="files")
router.register("leaveRequest", LeaveRequestViewSet)
router.register("leaveDetail", LeaveRequestDetailViewSet)

urlpatterns = [
    path("", include(router.urls)),
    #Request URL:
    # http://127.0.0.1:8000/leaveDetail/delete_multiple/?course_id=3&leave_request_id=30
    # Request Method:
    # DELETE
    path('leaveDetail/delete_multiple/', LeaveRequestDetailViewSet.as_view({'delete': 'delete_multiple'})),
]
