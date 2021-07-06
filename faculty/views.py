from django.shortcuts import render, HttpResponse


# Create your views here.
def login(request):
    return render(request, 'faculty/login.html')


def dashboard(request):
    return render(request, 'faculty/dashboard.html')

def add_subject(request):
    return render(request, 'faculty/add-subject.html')
