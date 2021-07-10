from django.db import models

from administrator.models import Institute
from subject.models import Subject
from student.models import student as Student


class Assignment(models.Model):
    no = models.PositiveIntegerField(unique=True)
    question = models.CharField(max_length=400)
    deadline = models.DateTimeField(auto_now=True, null=False, blank=False)
    assigned_date = models.DateTimeField(auto_now=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=0)

    def __str__(self):
        return f'Assignment-{self.no}@{self.subject.institute}'


class AssignmentInstance(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submit_time = models.DateTimeField(auto_now=True)
    file_uploaded = models.FileField(
        upload_to=f'assignments/')
    marks = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.student.enroll_no}-{self.assignment}'
