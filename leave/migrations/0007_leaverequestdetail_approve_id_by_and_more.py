# Generated by Django 5.0 on 2024-03-23 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0006_remove_leaverequest_file_id_files_leave_request_id'),
        ('teacher', '0005_remove_teacher_department_remove_teacher_faculty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequestdetail',
            name='approve_id_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approve_id_by', to='teacher.teacher'),
        ),
        migrations.AlterField(
            model_name='leaverequestdetail',
            name='teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_id', to='teacher.teacher'),
        ),
    ]