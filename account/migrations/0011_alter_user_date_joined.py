# Generated by Django 5.0 on 2024-03-19 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 20, 20, 39, 327001, tzinfo=datetime.timezone.utc)),
        ),
    ]