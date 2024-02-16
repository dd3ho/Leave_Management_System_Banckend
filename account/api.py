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

@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "username": request.user.username,
            "user_id": request.user.user_id,
            "email": request.user.email,
            "role": request.user.role
        }
    )


# signup
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
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
                    department_id = data.get("department"),
                    faculty_id = data.get("faculty"),
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
                    department_id = data.get("department"),
                    faculty_id = data.get("faculty"),
                )
                student.save()
        else:
            print("ไม่พบ User")
        
    else:
        print("Signup fail: form error")
        print(form.errors)
        message = "error"
    return JsonResponse({"message": message})


@api_view(["POST"])
def editPassword(request):
    user = request.user

    form = PasswordChangeForm(data=request.POST, user=user)

    if form.is_valid():
        form.save()

        return JsonResponse({"message": "success"})
    else:
        return JsonResponse({"message": form.errors.as_json()}, safe=False)
