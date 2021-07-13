from django.shortcuts import render, HttpResponse
<<<<<<< HEAD

from mysite.decorators import allowed_users
from subject.models import Subject


=======
from faculty.models import faculty
from mysite.decorators import allowed_users
from subject.models import Subject
from subject.forms import SubjectForm
from administrator.models import Institute
>>>>>>> e5f6f45c01df474ed9294a266d4b5c36d1de4c38
@allowed_users(allowed_groups=['faculty'])
def add_subject(request):


    return render(request, 'faculty/add-subject.html')


@allowed_users(allowed_groups=['faculty'])
def all_subjects(request):
    subjects = Subject.objects.filter(faculty=request.user.faculty)
    return render(request, 'faculty/all-subjects.html', {'subjects': subjects})
<<<<<<< HEAD
=======


def add_subject(request):
    subjectForm = SubjectForm(request.POST)
    if subjectForm.is_valid():
        subject = subjectForm.save(commit=False)
        Faculty = request.user.faculty
        subject.Faculty = Faculty

        subjectForm.save()
    else:
        print("form is invalid")

    return render(request, 'faculty/add-subject.html', {'subjectForm': subjectForm})
>>>>>>> e5f6f45c01df474ed9294a266d4b5c36d1de4c38
