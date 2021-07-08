from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .forms import (
    UserForm,
    InstituteForm,
    AdministratorForm
)


# Create your views here.
def register(request):
    return render(request, 'administrator/register.html')


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

            # redirecting to login page
            return HttpResponseRedirect(reverse('administrator:login'))

        # invalid data sent via request
        context = {
            'user_form': user_form,
            'institute_form': institute_form,
            'administrator_form': administrator_form,
        }
        return render(request, 'administrator/register.html', context=context)


def login(request):
    return render(request, 'administrator/dashboard.html')


def create_faculty(request):
    return render(request, 'administrator/create-faculty.html')


def create_student(request):


    return render(request, 'administrator/create-student.html')


def edit_institute_profile(request):
    # TODO: update institute profile
    return render(request, 'administrator/edit-institute-profile.html')


def dashboard(request):
    return render(request, 'administrator/dashboard.html')
