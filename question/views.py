from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
# from.import forms, models
# from django.db.models import Sum
# from django.contrib.auth.models import Group
# from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.conf import settings
# from datetime import date, timedelta
# from django.db.models import Q
# from django.core.mail import send_mail
# from faculty import models as TMODEL
# from student import models as SMODEL
# from faculty import forms as TFORM
# from django import forms as SFORM
# from django.contrib.auth.models import User


def home_view(request):
    return render(request, 'quiz/index.html')


def is_faculty(user):
    return user.groups.filter(name='FACULTY').exists()


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()




@login_required(login_url='facultylogin')
def admin_course_view(request):
    return render(request, 'quiz/admin_course.html')

""""
@login_required(login_url='faculty/login')
def admin_add_course_view(request):
    courseForm = forms.CourseForm()
    if request.method == 'POST':
        courseForm = forms.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-course')
    return render(request, 'quiz/faculty_add_course.html', {'courseForm': courseForm})


@login_required(login_url='faculty/login')
def admin_view_course_view(request):
    courses = models.Course.objects.all()
    return render(request, 'quiz/faculty_view_course.html', {'courses': courses})


@login_required(login_url='faculty/login')
def delete_course_view(request, pk):
    course = models.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/admin-view-course')


@login_required(login_url='faculty/login')
def admin_question_view(request):
    return render(request, 'faculty/faculty_question.html')


@login_required(login_url='faculty/login')
def admin_add_question_view(request):
    questionForm = forms.QuestionForm()
    if request.method == 'POST':
        questionForm = forms.QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            course = models.Course.objects.get(id=request.POST.get('courseID'))
            question.course = course
            question.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-question')
    return render(request, 'faculty/faculty_add_question.html', {'questionForm': questionForm})


@login_required(login_url='faculty/login')
def admin_view_question_view(request):
    courses = models.Course.objects.all()
    return render(request, 'faculty/faculty_view_question.html', {'courses': courses})


@login_required(login_url='faculty/login')
def view_question_view(request, pk):
    questions = models.Question.objects.all().filter(course_id=pk)
    return render(request, 'faculty/see_question.html', {'questions': questions})


@login_required(login_url='faculty/login')
def delete_question_view(request, pk):
    question = models.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/faculty-view-question')


@login_required(login_url='facultylogin')
def admin_view_student_marks_view(request):
    students = SMODEL.Student.objects.all()
    return render(request, 'faculty/faculty_view_student_marks.html', {'students': students})


@login_required(login_url='faculty/login')
def admin_view_marks_view(request, pk):
    courses = models.Course.objects.all()
    response = render(request, 'faculty/faculty_view_marks.html', {'courses': courses})
    response.set_cookie('student_id', str(pk))
    return response


@login_required(login_url='faculty/login')
def admin_check_marks_view(request, pk):
    course = models.Course.objects.get(id=pk)
    student_id = request.COOKIES.get('student_id')
    student = SMODEL.Student.objects.get(id=student_id)
    results = models.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request, 'faculty/faculty_check_marks.html', {'results': results})
"""