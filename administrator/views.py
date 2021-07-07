from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.views import View
from mysite.decorators import allowed_users
from .forms import (
    UserForm,
    InstituteForm,
    AdministratorForm
)


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

            if user:
                auth.login(request, user)
                return redirect('administrator:dashboard')
            else:
                return render(request, 'administrator/login.html')

        return render(request, 'administrator/login.html')


def create_faculty(request):
    return render(request, 'administrator/create-faculty.html')


def create_student(request):
    return render(request, 'administrator/create-student.html')


def edit_institute_profile(request):
    # TODO: update institute profile
    return render(request, 'administrator/edit-institute-profile.html')


@allowed_users(allowed_groups=['administrator'])
def dashboard(request):
    return render(request, 'administrator/dashboard.html')


@login_required(login_url='administrator:login')
def logout(request):
    auth.logout(request)
    return redirect('administrator:login')
