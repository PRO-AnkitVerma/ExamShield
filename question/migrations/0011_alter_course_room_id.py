# Generated by Django 3.2.5 on 2021-07-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0010_alter_course_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='room_id',
            field=models.CharField(blank=True, default='room-wpHYj', max_length=10),
        ),
    ]
