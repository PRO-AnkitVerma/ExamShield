from django.shortcuts import render, HttpResponse

from mysite.decorators import allowed_users
from subject.models import Subject


@allowed_users(allowed_groups=['faculty'])
def add_subject(request):


    return render(request, 'faculty/add-subject.html')


@allowed_users(allowed_groups=['faculty'])
def all_subjects(request):
    subjects = Subject.objects.filter(faculty=request.user.faculty)
    return render(request, 'faculty/all-subjects.html', {'subjects': subjects})
