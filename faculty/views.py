from django.shortcuts import render, HttpResponse


# Create your views here.
def login(request):
    return render(request, 'faculty/login.html')


def dashboard(request):
    return render(request, 'faculty/dashboard.html')

def add_subject(request):
    return render(request, 'faculty/add-subject.html')

def faculty_question(request):
    return render(request, 'faculty/faculty-question.html')

def faculty_add_question(request):
    return render(request, 'faculty/faculty-add-question.html')

def faculty_view_question(request):
    return render(request, 'faculty/faculty-view-question.html')

def see_question(request):
    return render(request, 'faculty/see-question.html')

def faculty_add_exam(request):
    return render(request, 'faculty/faculty-add-exam.html')

def faculty_view_exam(request):
    return render(request, 'faculty/faculty-view-exam.html')

def faculty_exam(request):
    return render(request, 'faculty/faculty-exam.html')