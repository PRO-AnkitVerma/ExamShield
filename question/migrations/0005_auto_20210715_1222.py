# Generated by Django 3.2.5 on 2021-07-15 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20210715_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]