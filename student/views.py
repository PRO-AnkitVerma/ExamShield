from datetime import datetime, timedelta
from random import shuffle

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from mysite.decorators import allowed_users
from question import models as QMODEL
from question.models import Result, Course
from student import models


class Login(View):
    def get(self, request):
        return render(request, 'student/login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user and user.groups.filter(name='student'):
                auth.login(request, user)
                return redirect('student:dashboard')
            else:
                messages.error(request, 'Error: Invalid Credentials!')
                return render(request, 'student/login.html')

        messages.warning(request, 'Please enter credentials to login')
        return render(request, 'student/login.html')


@login_required(login_url='student:login')
def logout(request):
    auth.logout(request)
    return redirect('student:login')


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


@allowed_users(allowed_groups=['student'])
def student_dashboard_view(request):
    context = {

        'total_course': QMODEL.Course.objects.all().count(),
        'total_question': QMODEL.Question.objects.all().count(),
        'institute': request.user.student.institute.name,
    }
    return render(request, 'student/dashboard.html', context=context)


@allowed_users(allowed_groups=['student'])
def student_marks_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'student/student-marks.html', {'courses': courses})


@allowed_users(allowed_groups=['student'])
def start_exam_view(request, pk):
    course = get_object_or_404(Course, id=pk)

    # can't give exam if exam is over!
    time_left = course.end_time - datetime.now()
    if time_left <= timedelta(microseconds=0):
        messages.info(request, f'Exam for {course.course_name} is over!')
        return redirect('student:student-exam')

    # can't give same exam twice!
    student = request.user.student
    if student.result_set.filter(exam=course):
        messages.info(request, f'You have already given exam for {course.course_name}!')
        return redirect('student:student-exam')

    # for testing purpose only
    time_left = timedelta(minutes=3)

    # getting time left in req format
    hours, mins, secs = str(time_left).split()[-1].split(':')
    hours = '0' + hours if len(hours) == 1 else hours
    mins = '0' + mins if len(mins) == 1 else mins
    secs = '0' + secs if len(secs) == 1 else secs

    questions = QMODEL.Question.objects.filter(course=course)
    total_questions = questions.count()

    # shuffling questions
    questions = list(questions)
    shuffle(questions)

    context = {
        'course': course,
        'questions': questions,
        'total_questions': total_questions,
        'hours': hours,
        'mins': mins,
        'secs': secs,
        'student': request.user.student,
    }
    return render(request, 'student/start-exam.html', context=context)


@allowed_users(allowed_groups=['student'])
def take_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    total_questions = QMODEL.Question.objects.all().filter(course=course).count()
    questions = QMODEL.Question.objects.all().filter(course=course)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks

    return render(request, 'student/take-exam.html',
                  {'course': course, 'total_questions': total_questions, 'total_marks': total_marks})


@allowed_users(allowed_groups=['student'])
def student_exam_view(request):
    student = request.user.student
    courses = Course.objects.filter(subject__institute=student.institute).order_by('-start_time')
    return render(request, 'student/student-exam.html', {'courses': courses})


@allowed_users(allowed_groups=['student'])
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = QMODEL.Course.objects.get(id=course_id)

        total_marks = 0
        questions = QMODEL.Question.objects.all().filter(course=course)
        for i in range(len(questions)):

            selected_ans = request.COOKIES.get(str(i + 1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = models.student.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks = total_marks
        result.exam = course
        result.student = student
        result.save()

        return HttpResponseRedirect('view-result')


@allowed_users(allowed_groups=['student'])
def view_result_view(request):
    student = request.user.student
    results = Result.objects.filter(student=student).order_by('-date')
    return render(request, 'student/view-result.html', context={
        'results': results
    })


@allowed_users(allowed_groups=['student'])
def check_marks_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    student = models.student.objects.get(user_id=request.user.id)
    results = QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request, 'student/check-marks.html', {'results': results})


@allowed_users(allowed_groups=['student'])
def save_result(request, course_id):
    if request.method != 'POST':
        return HttpResponse('BAD REQUEST')

    student = request.user.student
    marks = request.POST.get('total_score', '')
    course_id = course_id
    submitted_time = request.POST.get('time_submitting', '')

    try:
        course = Course.objects.get(id=course_id)
        Result.objects.create(
            student=student,
            marks=marks,
            exam=course,
            date=submitted_time,
            is_given=True,
        )
        return redirect('student:view-result')
    except Exception as e:
        return HttpResponse('Unable to save result!')


@allowed_users(allowed_groups=['student'])
def student_viva_view(request):
    return render(request, 'student/student-viva.html')
