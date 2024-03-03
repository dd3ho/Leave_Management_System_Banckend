# Generated by Django 5.0 on 2024-03-03 06:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_department_faculty_remove_course_teacher_id_and_more'),
        ('leave', '0001_initial'),
        ('teacher', '0005_remove_teacher_department_remove_teacher_faculty_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('leave_type', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('approve', 'Approved'), ('reject', 'Rejected'), ('pending', 'Pending')], default='pending', max_length=20)),
                ('approve_id_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
                ('file_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leave_papers', to='leave.files')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequestDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.course')),
                ('leave_request_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leave.leaverequest')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teacher_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]
