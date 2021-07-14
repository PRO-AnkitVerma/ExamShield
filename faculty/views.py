from django.contrib import auth, messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views import View

from mysite.decorators import allowed_users
from question import models as QMODEL
from student import models as SMODEL
from django import forms as QFORM

# Create your views here.
from question.views import is_faculty


class Login(View):
    def get(self, request):
        return render(request, 'faculty/login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user and user.groups.filter(name='faculty'):
                auth.login(request, user)
                return redirect('faculty:dashboard')
            else:
                messages.error(request, 'Error: Invalid Credentials!')
                return render(request, 'faculty/login.html')

        messages.warning(request, 'Please enter credentials to login')
        return render(request, 'faculty/login.html')


@login_required(login_url='faculty:login')
def logout(request):
    auth.logout(request)
    return redirect('faculty:login')


@allowed_users(allowed_groups=['faculty'])
def dashboard(request):
    faculty = request.user
    return render(request, 'faculty/dashboard.html', {
        'faculty': faculty,
        'institute': request.user.faculty.institute.name,
    })

#
# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
# def faculty_exam_view(request):
#     return render(request, 'faculty/faculty_exam.html')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
# def faculty_add_exam_view(request):
#     courseForm = QFORM.CourseForm()
#     if request.method == 'POST':
#         courseForm = QFORM.CourseForm(request.POST)
#         if courseForm.is_valid():
#             courseForm.save()
#         else:
#             print("form is invalid")
#         return HttpResponseRedirect('/faculty/faculty-view-exam')
#     return render(request, 'faculty/faculty_add_exam.html', {'courseForm': courseForm})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
# def faculty_view_exam_view(request):
#     courses = QMODEL.Course.objects.all()
#     return render(request, 'faculty/faculty_view_exam.html', {'courses': courses})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
# def delete_exam_view(request, pk):
#     course = QMODEL.Course.objects.get(id=pk)
#     course.delete()
#     return HttpResponseRedirect('/faculty/faculty-view-exam')


# @login_required(login_url='faculty/login')
# def faculty_question_view(request):
#     return render(request, 'faculty/faculty_question.html')


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
# def faculty_add_question_view(request):
#     questionForm = QFORM.QuestionForm()
#     if request.method == 'POST':
#         questionForm = QFORM.QuestionForm(request.POST)
#         if questionForm.is_valid():
#             question = questionForm.save(commit=False)
#             course = QMODEL.Course.objects.get(id=request.POST.get('courseID'))
#             question.course = course
#             question.save()
#         else:
#             print("form is invalid")
#         return HttpResponseRedirect('/faculty/faculty-view-question')
#     return render(request, 'faculty/faculty_add_question.html', {'questionForm': questionForm})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
# def faculty_view_question_view(request):
#     courses = QMODEL.Course.objects.all()
#     return render(request, 'faculty/faculty_view_question.html', {'courses': courses})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
# def see_question_view(request, pk):
#     questions = QMODEL.Question.objects.all().filter(course_id=pk)
#     return render(request, 'faculty/see_question.html', {'questions': questions})


# @login_required(login_url='faculty/login')
# @user_passes_test(is_faculty)
# def remove_question_view(request, pk):
#     question = QMODEL.Question.objects.get(id=pk)
#     question.delete()
#     return HttpResponseRedirect('/faculty/faculty-view-question')
