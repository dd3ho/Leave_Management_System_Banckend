# Generated by Django 5.0 on 2024-03-23 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0007_leaverequestdetail_approve_id_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='approve_id_by',
        ),
    ]
