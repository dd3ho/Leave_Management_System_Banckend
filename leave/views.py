from rest_framework import viewsets
from .models import Files, LeaveRequest, LeaveRequestDetail
from .serializer import FileSerializer, LeaveRequestSerializer, LeaveRequestDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
# ... your other imports


class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer


class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    
    # GET /leaveRequest/
    # GET /leaveRequest/?approve_id_by=12&status=approved
    # GET /leaveRequest/?status=approved
    # GET /leaveRequest/?approve_id_by=12

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id')
        approve_id_by = self.request.query_params.get('approve_id_by')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        leave_type = self.request.query_params.get('leave_type')
        status = self.request.query_params.get('status')

        if approve_id_by:
            queryset = queryset.filter(approve_id_by=approve_id_by)

        if start_date:
            queryset = queryset.filter(start_date__icontains=start_date)
            
        if end_date:
            queryset = queryset.filter(end_date__icontains=end_date)
        
        if leave_type:
            queryset = queryset.filter(leave_type__icontains=leave_type)
        
        if status:
            queryset = queryset.filter(status__icontains=status)
        
        if id:
            queryset = queryset.filter(id=id)
        
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            leaveRequest = serializer.save()  # save the instance and return the model instance
            lid = leaveRequest.id  # access the id of the model instance

            # You're trying to build a URL with the leaveRequest.id which is correct.
            leaveRequest_url = f'http://localhost:8000/leaveRequest/{lid}/'
            leaveRequest_id = lid

            # At this point, serializer.data is a ReturnDict which cannot be updated with new keys as you intend.
            # Instead, build a new response dictionary based on serializer.data
            response_data = serializer.data
            response_data['id-url'] = leaveRequest_url  # Add the URL to the serialized data
            response_data['leaveRequest_id'] = leaveRequest_id
            
            return Response(response_data, status=status.HTTP_201_CREATED)  # Return the updated data
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        try:
            # 'pk' is typically the URL keyword argument for the primary key of the model
            leave_request = LeaveRequest.objects.get(pk=kwargs.get('pk'))
            leave_request.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except LeaveRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle unexpected errors
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # def create(self, request):
    #     serializer = LeaveRequestSerializer(data=request.data)
    #     if serializer.is_valid():
    #         leaveRequest = serializer.save()
    #         lid = leaveRequest.id
    #         leaveRequest.url = f'http://localhost:8000/leaveRequest/{lid}/'
    #         data = serializer.data
    #         data.update({'id-url':leaveRequest.url}) # attaching key-value to the dictionary
    #         return Response(data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class LeaveRequestDetailViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequestDetail.objects.all()
    serializer_class = LeaveRequestDetailSerializer
    
    # GET /leaveDetail/
    # GET /leaveDetail/?approve_id_by=12&status=approved
    # GET /leaveDetail/?status=approved
    # GET /leaveDetail/?approve_id_by=12
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        leave_request_id = self.request.query_params.get('leave_request_id')
        student_id = self.request.query_params.get('student_id')
        teacher_id = self.request.query_params.get('teacher_id')
        course_id = self.request.query_params.get('course_id')
        
        
        if leave_request_id:
            queryset = queryset.filter(leave_request_id_by=leave_request_id)
        
        if teacher_id:
            queryset = queryset.filter(teacher_id=teacher_id)
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        if student_id:
            queryset = queryset.filter(student_id=student_id)
        
        return queryset
    
    def destroy(self, request, *args, **kwargs):
        try:
            # Extract 'course_id' and 'leave_request_id' from the request if they are provided
            course_id = request.query_params.get('course_id')
            leave_request_id = request.query_params.get('leave_request_id')
            
            if course_id and leave_request_id:
                # Filter the queryset for all records with the given 'course_id' and 'leave_request_id'
                leave_request_details = LeaveRequestDetail.objects.filter(
                    course_id=course_id,
                    leave_request_id=leave_request_id
                )
                # If no records are found, return a 404 response
                if not leave_request_details.exists():
                    return Response(status=status.HTTP_404_NOT_FOUND)
                # Delete all records in the queryset
                leave_request_details.delete()
            else:
                # If 'course_id' or 'leave_request_id' is not provided, just delete the single object
                leave_request_detail = self.get_object()
                leave_request_detail.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except LeaveRequestDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle unexpected errors
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['delete'])
    def delete_multiple(self, request):
        course_id = request.query_params.get('course_id')
        leave_request_id = request.query_params.get('leave_request_id')
        
        if course_id and leave_request_id:
            LeaveRequestDetail.objects.filter(
                course_id=course_id,
                leave_request_id=leave_request_id
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
