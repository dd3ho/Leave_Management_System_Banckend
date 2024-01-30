# views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         user = request.user
#         old_password = request.POST.get('oldPassword')
#         new_password = request.POST.get('newPassword')
#         confirm_new_password = request.POST.get('confirmNewPassword')

#         # ตรวจสอบว่ารหัสผ่านเดิมถูกต้องหรือไม่
#         if user.check_password(old_password):
#             # ตรวจสอบว่ารหัสผ่านใหม่ตรงกันหรือไม่
#             if new_password == confirm_new_password:
#                 # เปลี่ยนรหัสผ่าน
#                 user.set_password(new_password)
#                 user.save()
#                 return JsonResponse({'message': 'Password changed successfully'}, status=200)
#             else:
#                 return JsonResponse({'error': 'New passwords do not match'}, status=400)
#         else:
#             return JsonResponse({'error': 'Invalid old password'}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=400)
