# Generated by Django 3.2.5 on 2021-07-04 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
