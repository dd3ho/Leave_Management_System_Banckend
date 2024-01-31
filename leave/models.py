from django.db import models
from account.models import User


# Create your models here.
class Files(models.Model):
    pdf = models.FileField(upload_to="store/pdfs/")

    def __str__(self):
        return self.pdf


class LeavePaper(models.Model):
    student_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    subjects = models.JSONField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    leave_type = models.CharField(max_length=20)
    file_id =models.name = models.ForeignKey(Files, related_name='leave_papers', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
