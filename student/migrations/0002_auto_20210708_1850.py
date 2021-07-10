# Generated by Django 3.2.5 on 2021-07-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_alter_subject_name'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='enroll_no',
            field=models.PositiveIntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(to='subject.Subject'),
        ),
    ]