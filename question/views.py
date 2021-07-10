from django.shortcuts import render, HttpResponse



# Create your views here.

def faculty_question(request):
    return render(request, 'quiz/faculty-question.html')

def faculty_add_question(request):
    return render(request, 'quiz/faculty-add-question.html')

def faculty_view_question(request):
    return render(request, 'quiz/faculty-view-question.html')

def see_question(request):
    return render(request, 'quiz/see-question.html')

def faculty_add_exam(request):
    return render(request, 'quiz/faculty-add-exam.html')

def faculty_view_exam(request):
    return render(request, 'quiz/faculty-view-exam.html')

def faculty_exam(request):
    return render(request, 'quiz/faculty-exam.html')