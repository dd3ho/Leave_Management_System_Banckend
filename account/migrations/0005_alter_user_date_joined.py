# Generated by Django 5.0 on 2024-01-29 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 30, 5, 45, 19, 70515, tzinfo=datetime.timezone.utc)),
        ),
    ]
