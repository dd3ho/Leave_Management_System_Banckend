# Generated by Django 5.0 on 2024-01-30 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 30, 15, 21, 8, 649187, tzinfo=datetime.timezone.utc)),
        ),
    ]