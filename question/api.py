from django.http import HttpResponse
from django.core import serializers

from question.models import Course, Question


def get_course(request, course_id):
    course = Course.objects.filter(id=course_id)
    data = serializers.serialize('json', course)
    return HttpResponse(data, content_type='text/json-comment-filtered')


def get_all_questions(request, course_id):
    questions = Question.objects.filter(course__id=course_id)
    data = serializers.serialize('json', questions)
    return HttpResponse(data, content_type='text/json-comment-filtered')
