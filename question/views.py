from django.shortcuts import render, HttpResponse
from question.models import Course
from question.models import Question
from subject.models import Subject


# Create your views here.

def faculty_question(request):
    return render(request, 'quiz/faculty-question.html')

def faculty_add_question(request):
    if request.method == 'POST':
        question = request.POST.get('question', 'default')
        marks = request.POST.get('marks', 'default')
        option1 = request.POST.get('option1', 'default')
        option2 = request.POST.get('option2', 'default')
        option3 = request.POST.get('option3', 'default')
        option4 = request.POST.get('option4', 'default')
        answer = request.POST.get('answer', 'default')

        add_question = Question(question=question, marks=marks, option1=option1, option2=option2, option3=option3, option4=option4, answer=answer)
        add_question.save()
    return render(request, 'quiz/faculty-add-question.html')

def faculty_view_question(request):
    return render(request, 'quiz/faculty-view-question.html')

def see_question(request):
    return render(request, 'quiz/see-question.html')

def faculty_add_exam(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name', 'default')
        question_number = request.POST.get('question_number', 'default')
        total_marks = request.POST.get('total_marks', 'default')
        print(course_name, question_number, total_marks)
        course = Course(course_name=course_name, question_number=question_number, total_marks=total_marks)
        course.save()
    return render(request, 'quiz/faculty-add-exam.html')

def faculty_view_exam(request):
    return render(request, 'quiz/faculty-view-exam.html')

def faculty_exam(request):
    return render(request, 'quiz/faculty-exam.html')