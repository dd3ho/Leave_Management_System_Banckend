# Generated by Django 5.0 on 2024-03-03 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 3, 13, 17, 33, 722170, tzinfo=datetime.timezone.utc)),
        ),
    ]