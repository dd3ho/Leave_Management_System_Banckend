# Generated by Django 4.2.7 on 2024-03-05 14:01

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
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 5, 21, 1, 6, 869161, tzinfo=datetime.timezone.utc)),
        ),
    ]
