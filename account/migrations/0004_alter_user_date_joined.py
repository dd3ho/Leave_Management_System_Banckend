# Generated by Django 5.0 on 2024-02-18 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_date_joined_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 18, 20, 9, 22, 638182, tzinfo=datetime.timezone.utc)),
        ),
    ]
