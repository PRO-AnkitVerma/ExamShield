from django.db import models

from administrator.models import Institute
from faculty.models import faculty as Faculty


class Subject(models.Model):
    code = models.IntegerField(null=True, blank=True, help_text='Enter subject code')
    name = models.CharField(max_length=200, help_text='Enter subject name', null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
    institute = models.ForeignKey(Institute, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name}@{self.faculty}'
