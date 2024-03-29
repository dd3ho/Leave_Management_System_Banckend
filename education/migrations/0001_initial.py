# Generated by Django 5.0 on 2024-01-29 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=10)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]
