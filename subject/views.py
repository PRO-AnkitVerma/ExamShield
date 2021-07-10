from django.shortcuts import render, HttpResponse
from subject.models import Subject

def add_subject(request):
    if request.method=='POST':
        code = request.POST['code']
        name = request.POST['name']
        subject = Subject(name=name, code=code)
        subject.save()
    return render(request, 'faculty/add-subject.html')
