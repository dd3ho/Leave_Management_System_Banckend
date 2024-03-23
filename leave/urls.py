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
    path('leaveDetail/update_multiple/', LeaveRequestDetailViewSet.as_view({'put': 'update_multiple'})),
    # เพิ่ม path สำหรับ update_approve_id_by ใน LeaveRequestDetailViewSet
    # path('leaveRequest/<int:pk>/update_approve_id_by/', LeaveRequestViewSet.as_view({'put': 'update_approve_id_by'})),
]
