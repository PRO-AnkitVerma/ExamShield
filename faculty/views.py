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


@allowed_users(allowed_groups=['faculty'])
def video_conference(request):
    return render(request, 'faculty/faculty-video-conference.html')
