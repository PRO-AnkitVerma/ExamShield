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
    return user.groups.filter(name='FACULTY').exists()


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


@login_required(login_url='facultylogin')
def admin_course_view(request):
    return render(request, 'quiz/admin_course.html')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
@allowed_users(allowed_groups=['faculty'])
def faculty_exam_view(request):
    return render(request, 'quiz/faculty-exam.html')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def faculty_view_exam_view(request):
    courses = Course.objects.all()
    return render(request, 'quiz/faculty-view-exam.html', {'courses': courses})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def delete_exam_view(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/question/faculty-view-exam')


# @login_required(login_url='faculty/login')
def faculty_question_view(request):
    return render(request, 'quiz/faculty-question.html')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
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


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def faculty_view_question_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'quiz/faculty-view-question.html', {'courses': courses})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def see_question_view(request, pk):
    questions = QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request, 'question/see-question.html', {'questions': questions})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def remove_question_view(request, pk):
    question = QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/question/faculty-view-question')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def faculty_view_exam(request):
    return render(request, 'quiz/faculty-exam.html')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def faculty_add_exam_view(request):
    # TODO: Here on exam to question
    if request.method == 'GET':
        return render(request, 'quiz/test.html', context={
            'courseForm': CourseForm(),
            'subjects': Subject.objects.filter(faculty=request.user.faculty),
        })

    if request.method == 'POST':
        subject_id = request.POST.get('subject_id', '')
        courseForm = CourseForm(request.POST)
        if courseForm.is_valid() and subject_id:
            course = courseForm.save(commit=False)
            course.subject = Subject.objects.get(id=subject_id)
            course = course.save()
            print('Hello:', course.course_name, 'bye')
            return render(request, 'quiz/faculty-add-question.html', context={'course': course.course_name})
        else:
            # TODO: Fix it!
            return HttpResponse('Try Unsuccessful!')

        return HttpResponseRedirect('question/faculty-view-exam')

    # elif request.method == 'GET':
    #     courseForm = CourseForm()
    # 
    #     return render(request, 'quiz/test.html', {
    #         'subjects': Subject.objects.filter(faculty=request.user.faculty),
    #         'courseForm': courseForm
    #     })

    else:
        return HttpResponse('BAD REQUEST!')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def faculty_view_exam(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'quiz/faculty_view_exam.html', {'courses': courses})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def delete_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/question/faculty-view-exam')


# @login_required(login_url='faculty/login')
def faculty_question_view(request):
    return render(request, 'quiz/faculty-question.html')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
@allowed_users(allowed_groups=['faculty'])
def faculty_add_question_view(request):
    return HttpResponse('Faculty - Add - Question')
    # questionForm = QuestionForm()
    # if request.method == 'POST':
    #     questionForm = QuestionForm(request.POST)
    #     if questionForm.is_valid():
    #         question = questionForm.save(commit=False)
    #         course = QMODEL.Course.objects.get(id=request.POST.get('courseID'))
    #         question.course = course
    #         question.save()
    #         return render(request, 'quiz/faculty-add-question.html', {'questionForm': questionForm})
    #
    #     else:
    #         print("form is invalid")
    #         return render(request, 'quiz/faculty-add-question.html', {'questionForm': questionForm})

    return HttpResponseRedirect('/question/faculty-view-question')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def faculty_view_question_view(request):
    courses = QMODEL.Course.objects.all()
    print("helo")
    return render(request, 'quiz/faculty-view-question.html', {
        'courses': courses
    })


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def see_question_view(request, pk):
    questions = QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request, 'quiz/see-question.html', {'questions': questions})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
def remove_question_view(request, pk):
    question = QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/question/faculty-view-question')
