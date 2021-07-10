from django.contrib.auth.models import User
from django.db import models
from administrator.models import Institute
from subject.models import Subject


class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=False, blank=False)
    enroll_no = models.PositiveIntegerField(unique=True, null=False, blank=False)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f'student-{self.enroll_no}@{self.institute.name}'
