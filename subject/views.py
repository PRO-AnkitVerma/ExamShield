from django.shortcuts import render, HttpResponse
from faculty.models import faculty as FMODEL
from mysite.decorators import allowed_users
from subject.models import Subject
from subject.forms import SubjectForm
from administrator.models import Institute


@allowed_users(allowed_groups=['faculty'])
def add_subject(request):
    return render(request, 'faculty/add-subject.html')


@allowed_users(allowed_groups=['faculty'])
def all_subjects(request):
    subjects = Subject.objects.filter(faculty=request.user.faculty)
    return render(request, 'faculty/all-subjects.html', {'subjects': subjects})


@allowed_users(allowed_groups=['faculty'])
def add_subject(request):
    subjectForm = SubjectForm(request.POST)

    if subjectForm.is_valid():
        subject = subjectForm.save(commit=False)
        subject.faculty = request.user.faculty
        subject.institute = request.user.faculty.institute
        subject.save()

        return render(request, 'faculty/add-subject.html', context={'subjectForm': subjectForm})

    else:
        print("form is invalid")

    return render(request, 'faculty/all-subject.html', {'subjectForm': subjectForm})
