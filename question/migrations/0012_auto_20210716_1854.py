# Generated by Django 3.2.5 on 2021-07-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0011_alter_course_room_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='question_number',
        ),
        migrations.AlterField(
            model_name='course',
            name='room_id',
            field=models.CharField(blank=True, default='room-eLFtf', max_length=10),
        ),
    ]
