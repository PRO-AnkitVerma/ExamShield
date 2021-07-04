from django.contrib.auth.models import User
from django.db import models


class Institute(models.Model):
    name = models.CharField(max_length=200,
                            null=False,
                            blank=False,
                            help_text='Enter name of institute')
    code = models.IntegerField(null=True, blank=True, help_text='Enter institute code')
    city = models.CharField(max_length=200, help_text='Enter city')
    state = models.CharField(max_length=200, help_text='Enter state')
    country = models.CharField(max_length=200, help_text='Enter country')

    # TODO: add attributes: website, type, unique code autogenerate

    def __str__(self):
        return self.name


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institute = models.OneToOneField('Institute', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.user}@{self.institute.name}'
