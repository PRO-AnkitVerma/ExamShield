# Generated by Django 3.2.5 on 2021-07-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_assignmentinstance_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='reference',
            field=models.FileField(blank=True, null=True, upload_to='reference/'),
        ),
    ]