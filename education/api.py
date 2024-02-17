from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .forms import SignupForm
from django.contrib.auth.forms import PasswordChangeForm
from teacher.models import Teacher
from student.models import Student
from account.models import User
from education.models import Faculty, Department

# @api_view(["GET"])
# def me(request):
#     return JsonResponse(
#         {
#             "id": request.user.id,
#             "username": request.user.username,
#             "user_id": request.user.user_id,
#             "email": request.user.email,
#             "role": request.user.role
#         }
#     )


# signup
@api_view(["POST"])
@authentication_classes([]) # บอกให้ DRF ไม่ใช้ Authentication classes ใดๆ กับ view นี้
@permission_classes([]) # บอกให้ DRF ไม่ใช้ Permission classes ใดๆ กับ view นี้
def signup(request):
    data = request.data
    message = "success"

    form = SignupForm(
        {
            "username": data.get("username"),
            "user_id": data.get("user_id"),
            "email": data.get("email"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
            "role": data.get("role")
        }
    )


    if form.is_valid():
        print("Already save User")
        form.save()
        role = data.get("role")
        
        # ตรวจสอบว่ามีผู้ใช้งานอยู่แล้วหรือไม่
        try:
            user = User.objects.get(username= data.get("username"))
        except User.DoesNotExist:
            user = None
            
        faculty_id = data.get("faculty_id")
        department_id = data.get("department_id")
        
        if faculty_id == "":
            faculty = None
            if department_id == "":
                department = None
            else:
                department = Department.objects.get(id=data.get("department_id"))
        else:
            if department_id == "":
                department = None
            else:
                faculty = Faculty.objects.get(id=data.get("faculty_id"))
                department = Department.objects.get(id=data.get("department_id"))
                

        # try:
        #     faculty = Faculty.objects.get(id=data.get("faculty_id"))
        # except Faculty.DoesNotExist:
        #     faculty = None
    
        # try:
        #     department = Department.objects.get(id=data.get("department_id"))
        # except Department.DoesNotExist:
        #     department = None

        if user:
            if role == "teacher":

                '''
                create a new teacher
                '''
                teacher = Teacher(
                    user_id = User.objects.get(id=user.id),
                    prefix = data.get("prefix"),
                    fname = data.get("fname"),
                    lname = data.get("lname"),
                    faculty_id = faculty,
                    department_id = department,
                )
                teacher.save()
            else:
                '''
                create a new Student
                '''
                student = Student(
                    user_id = User.objects.get(id=user.id),
                    prefix = data.get("prefix"),
                    fname = data.get("fname"),
                    lname = data.get("lname"),
                    faculty_id = faculty,
                    department_id = department
                )
                student.save()
        else:
            print("ไม่พบ User")
        
    else:
        print("Signup fail: form error")
        print(form.errors)
        message = "error"
    return JsonResponse({"message": message})
