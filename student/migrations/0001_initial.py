# Generated by Django 5.0 on 2024-02-16 17:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0002_department_faculty_remove_course_teacher_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, max_length=20, null=True)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('department_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.department')),
                ('faculty_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.faculty')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegisterCourser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
