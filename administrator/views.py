from django.shortcuts import render, HttpResponse


# Create your views here.
def register(request):
    return render(request, 'administrator/register.html')


def login(request):
    return render(request, 'administrator/login.html')


def create_faculty(request):
    return render(request, 'administrator/create-faculty.html')


def create_student(request):
    return render(request, 'administrator/create-student.html')


def edit_institute_profile(request):
    return render(request, 'administrator/edit-institute-profile.html')


def dashboard(request):
    return render(request, 'administrator/dashboard.html')
