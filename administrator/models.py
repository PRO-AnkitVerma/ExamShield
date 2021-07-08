from django.contrib.auth.models import User
from django.db import models


class Institute(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, help_text='Enter name of institute')
    code = models.IntegerField(null=True, blank=True, help_text='Enter institute code')
    city = models.CharField(max_length=200, help_text='Enter city', null=True, blank=True)
    state = models.CharField(max_length=200, help_text='Enter state', null=True, blank=True)
    country = models.CharField(max_length=200, help_text='Enter country', null=True, blank=True)
    website_url = models.URLField(max_length=200, help_text='Enter website url', null=True, blank=True)

    def __str__(self):
        return self.name


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institute = models.OneToOneField('Institute', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.user}@{self.institute.name}'
class StudentInfo(models.Model):
    user=models.CharField(max_length=200,
                            null=False,
                            blank=False,
                            help_text='Enter ID')
    institute = models.OneToOneField('Institute', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}@{self.institute.name}'

class FacultyInfo(models.Model):
    user=models.CharField(max_length=200,
                            null=False,
                            blank=False,
                            help_text='Enter faculty ID')
    institute = models.OneToOneField('Institute', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}@{self.institute.name}'
