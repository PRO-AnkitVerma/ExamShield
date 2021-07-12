from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from mysite.decorators import allowed_users
from question import models as QMODEL
# from django import forms as QFORM
from question.forms import CourseForm, QuestionForm
from question.models import Course
from faculty.models import faculty as Faculty
from subject.models import Subject


def home_view(request):
    return render(request, 'quiz/index.html')


def is_faculty(user):
    return user.groups.filter(name='faculty').exists()


def is_student(user):
    return user.groups.filter(name='student').exists()


def admin_course_view(request):
    return render(request, 'quiz/admin_course.html')


@allowed_users(allowed_groups=['faculty'])
def faculty_exam_view(request):
    return render(request, 'quiz/faculty-exam.html')


@allowed_users(allowed_groups=['faculty'])
def faculty_view_exam_view(request):
    courses = Course.objects.filter(subject__faculty=request.user.faculty)
    return render(request, 'quiz/faculty-view-exam.html', {'courses': courses})


@allowed_users(allowed_groups=['faculty'])
def delete_exam_view(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/question/faculty-view-exam')


@allowed_users(allowed_groups=['faculty'])
def faculty_question_view(request):
    return render(request, 'quiz/faculty-question.html')


@allowed_users(allowed_groups=['faculty'])
def faculty_add_question_view(request):
    questionForm = QuestionForm()
    if request.method == 'POST':
        questionForm = QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            course = QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course = course
            question.save()

        else:
            print("form is invalid")
        return HttpResponseRedirect('/question/faculty-view-question')

    return render(request, 'quiz/faculty-add-question.html', {'questionForm': questionForm})


@allowed_users(allowed_groups=['faculty'])
def faculty_view_question_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'quiz/faculty-view-question.html', {'courses': courses})


@allowed_users(allowed_groups=['faculty'])
def see_question_view(request, pk):
    questions = QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request, 'question/see-question.html', {'questions': questions})


@allowed_users(allowed_groups=['faculty'])
def remove_question_view(request, pk):
    question = QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/question/faculty-view-question')


@allowed_users(allowed_groups=['faculty'])
def faculty_view_exam(request):
    print('from view exam')
    return render(request, 'quiz/faculty-exam.html')

@allowed_users(allowed_groups=['faculty'])
def faculty_add_exam_view(request):
    # TODO: Here on exam to question
    if request.method == 'GET':
        return render(request, 'quiz/faculty-add-exam.html', context={
            'courseForm': CourseForm(),
            'subjects': Subject.objects.filter(faculty=request.user.faculty),
        })

    if request.method == 'POST':
        subject_id = request.POST.get('subject_id', '')
        courseForm = CourseForm(request.POST)

        # exam data is valid
        if courseForm.is_valid() and subject_id:
            course = courseForm.save(commit=False)
            course.subject = Subject.objects.get(id=subject_id)
            course.save()
            return render(request, 'quiz/faculty-add-question.html', context={'course': course})

        # invalid data passed!
        return render(request, 'quiz/faculty-add-exam.html', context={
            'courseForm': courseForm,
            'subjects': Subject.objects.filter(faculty=request.user.faculty),
        })

    return HttpResponse('BAD REQUEST!')
