# Generated by Django 5.0 on 2024-02-20 13:36

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
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 20, 20, 36, 54, 829937, tzinfo=datetime.timezone.utc)),
        ),
    ]
