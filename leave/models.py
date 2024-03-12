from django.db import models
from account.models import User
from education.models import Course
from teacher.models import Teacher
from student.models import Student

STATUS = [
    ("approve", "Approved"),
    ("reject", "Rejected"),
    ("pending", "Pending"),
]


TYPE = [
    ("ลากิจ", "Personal Leave"),
    ("ลาป่วย", "Sick Leave"),
    ("อื่น ๆ", "Other Leave"),
]

# Create your models here.

class LeaveRequest(models.Model):
    approve_id_by = models.ForeignKey(
        Teacher, null=True, blank=True,
        on_delete=models.CASCADE
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    leave_type = models.CharField(max_length=20, choices=TYPE, default="undefined")
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

class LeaveRequestDetail(models.Model):
    leave_request_id = models.ForeignKey(LeaveRequest, null=True, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default="pending")

    
    # subjects = models.JSONField()
    # start_date = models.DateField(null=True, blank=True)
    # end_date = models.DateField(null=True, blank=True)
    # leave_type = models.CharField(max_length=20)
    # file_id =models.name = models.ForeignKey(Files, related_name='leave_papers', on_delete=models.CASCADE)
    # description = models.TextField()
    # created_at = models.DateField(auto_now_add=True)
    # teachers = models.ManyToManyField(Teacher, null=True, blank=True)


class Files(models.Model):
    leave_request_id = models.ForeignKey(LeaveRequest, null=True, blank=True, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to="store/pdfs/")

    def __str__(self):
        return self.pdf
