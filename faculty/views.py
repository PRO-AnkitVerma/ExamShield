from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from question import models as QMODEL
from student import models as SMODEL
from django import forms as QFORM


# Create your views here.
from question.views import is_faculty


def login(request):
    return render(request,'faculty/login.html')

def dashboard(request):

    return render(request, 'faculty/dashboard.html')
