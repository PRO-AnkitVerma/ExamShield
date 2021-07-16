from django.db import models
from student.models import student as Student_from_database
from administrator.models import Institute
from subject.models import Subject
from datetime import datetime, timedelta
from utils.random_password import generate_random_password


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now, blank=True)
    end_time = models.DateTimeField(default=datetime.now, blank=True)
    room_id = models.CharField(default='room123', max_length=10, null=False, blank=False)

    def __str__(self):
        return self.course_name

    @property
    def question_number(self):
        return Question.objects.filter(course=self).count()

    @property
    def total_marks(self):
        return sum([question.marks for question in Question.objects.filter(course=self)])

    @property
    def time_left(self):
        return self.end_time - datetime.now()

    @property
    def exam_time(self):
        return self.end_time - self.start_time

    @property
    def status(self):
        if self.time_left <= timedelta(microseconds=0):
            return 'Finished'

        if self.time_left > self.exam_time:
            return 'Upcoming'

        return 'Ongoing'


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    cat = (('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'))
    answer = models.CharField(max_length=200, choices=cat)


class Result(models.Model):
    student = models.ForeignKey(Student_from_database, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    is_given = models.BooleanField(default=False)
