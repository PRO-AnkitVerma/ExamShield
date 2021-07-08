from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.urls import reverse
from django.views import View
from student.models import student as Student
from faculty.models import faculty as Faculty
from subject.models import Subject
from faculty.forms import FacultyForm
from student.forms import StudentForm
from mysite.decorators import allowed_users
from .models import Administrator, User
from .forms import (
    UserForm,
    InstituteForm,
    AdministratorForm
)
from utils.random_password import generate_random_password


class Register(View):
    def get(self, request):
        context = {
            'user_form': UserForm(),
            'institute_form': InstituteForm(),
            'administrator_form': AdministratorForm()
        }
        return render(request, 'administrator/register.html', context=context)

    def post(self, request):
        user_form = UserForm(data=request.POST)
        institute_form = InstituteForm(data=request.POST)
        administrator_form = AdministratorForm(data=request.POST)

        # all valid data send by request
        if user_form.is_valid() and institute_form.is_valid() and administrator_form.is_valid():
            # saving user
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = True
            user.is_staff = True
            user.save()

            # saving institute
            institute = institute_form.save()

            # saving administrator
            administrator = administrator_form.save(commit=False)
            administrator.user = user
            administrator.institute = institute
            administrator.save()

            # adding to administrator group
            administrator_group = Group.objects.get(name='administrator')
            administrator_group.user_set.add(administrator.user)

            # redirecting to login page
            return HttpResponseRedirect(reverse('administrator:login'))

        # invalid data sent via request
        context = {
            'user_form': user_form,
            'institute_form': institute_form,
            'administrator_form': administrator_form,
        }
        return render(request, 'administrator/register.html', context=context)


class Login(View):
    def get(self, request):
        return render(request, 'administrator/login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user and user.groups.filter(name='administrator'):
                auth.login(request, user)
                return redirect('administrator:dashboard')
            else:
                messages.error(request, 'Error: Invalid Credentials!')
                return render(request, 'administrator/login.html')

        messages.warning(request, 'Please enter credentials to login')
        return render(request, 'administrator/login.html')


@allowed_users(allowed_groups=['administrator'])
def create_faculty(request):
    password = generate_random_password()

    if request.method == 'GET':
        context = {
            'password': password,
            'faculty_form': FacultyForm(),
        }
        return render(request, 'administrator/create-faculty.html', context=context)

    elif request.method == 'POST':
        # getting data to create faculty
        faculty_password = request.POST.get('password', '')
        faculty_form = FacultyForm(data=request.POST)

        if faculty_form.is_valid() and faculty_password:
            # data is valid 
            faculty_username = faculty_form.cleaned_data['email']

            try:
                # creating faculty
                new_user = User.objects.create_user(username=faculty_username, password=faculty_password)
                faculty = faculty_form.save(commit=False)
                faculty.user = new_user
                faculty.institute = request.user.administrator.institute
                faculty.save()

                # adding faculty to faculty group
                faculty_group = Group.objects.get(name='faculty')
                faculty_group.user_set.add(faculty.user)

                messages.success(request, 'Faculty Created Successfully!')

            except IntegrityError as ie:
                # i.e if user exists in database
                messages.error(request,
                               f'Faculty can\'t be created! An user with username {faculty_username} already exists!')

            context = {
                'password': password,
                'faculty_form': FacultyForm(),
            }
            return render(request, 'administrator/create-faculty.html', context=context)

        else:
            # if invalid data passed
            context = {
                'password': password,
                'faculty_form': faculty_form,
            }

            error_message = f'''
            Faculty can't be created because
            {faculty_form.errors.as_text()}
            '''
            messages.error(request, error_message)
            return render(request, 'administrator/create-faculty.html', context=context)

    # tried requesting page using any other methods
    return HttpResponse('BAD REQUEST')


@allowed_users(allowed_groups=['administrator'])
def create_student(request):
    password = generate_random_password()

    if request.method == 'GET':
        context = {
            'password': password,
            'student_form': StudentForm(),
        }
        return render(request, 'administrator/create-student.html', context=context)

    elif request.method == 'POST':
        # getting data to create student
        student_password = request.POST.get('password', '')
        student_form = StudentForm(data=request.POST)

        if student_form.is_valid() and student_password:
            # data is valid
            student_username = student_form.cleaned_data['email']

            try:
                # creating student
                new_user = User.objects.create_user(username=student_username, password=student_password)
                student = student_form.save(commit=False)
                student.user = new_user
                student.institute = request.user.administrator.institute
                student.save()

                # adding student to student group
                student_group = Group.objects.get(name='student')
                student_group.user_set.add(student.user)

                messages.success(request, 'Student Created Successfully!')

            except IntegrityError as ie:
                # i.e if user exists in database
                messages.error(request,
                               f'Student can\'t be created! An user with username {student_username} already exists!')

            context = {
                'password': password,
                'student_form': StudentForm(),
            }
            return render(request, 'administrator/create-student.html', context=context)

        else:
            # if invalid data passed
            context = {
                'password': password,
                'student_form': student_form,
            }

            error_message = f'''
                Student can't be created because
                {student_form.errors.as_text()}
                '''
            messages.error(request, error_message)
            return render(request, 'administrator/create-student.html', context=context)

    # tried requesting page using any other methods
    return HttpResponse('BAD REQUEST')


@allowed_users(allowed_groups=['administrator'])
def edit_institute_profile(request):
    # TODO: update institute profile
    return render(request, 'administrator/edit-institute-profile.html')


@allowed_users(allowed_groups=['administrator'])
def dashboard(request):
    user = request.user

    context = {
        'user': user,
        'total_faculties': Faculty.objects.all().count(),
        'total_subjects': Subject.objects.all().count(),
        'total_students': Student.objects.all().count(),
        'institute': user.administrator.institute,
    }
    return render(request, 'administrator/dashboard.html', context=context)


@login_required(login_url='administrator:login')
def logout(request):
    auth.logout(request)
    return redirect('administrator:login')
