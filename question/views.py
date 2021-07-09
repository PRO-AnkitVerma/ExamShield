from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from question import models as QMODEL
from django import forms as QFORM

def home_view(request):
    return render(request, 'quiz/index.html')


def is_faculty(user):
    return user.groups.filter(name='FACULTY').exists()


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()




@login_required(login_url='facultylogin')
def admin_course_view(request):
    return render(request, 'quiz/admin_course.html')

#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_exam_view(request):
    return render(request, 'quiz/faculty_exam.html')


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_add_exam_view(request):
    courseForm = QFORM.CourseForm()
    if request.method == 'POST':
        courseForm = QFORM.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/question/faculty-view-exam')
    return render(request, 'quiz/faculty_add_exam.html', {'courseForm': courseForm})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_view_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'quiz/faculty_view_exam.html', {'courses': courses})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def delete_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/question/faculty-view-exam')


#@login_required(login_url='faculty/login')
def faculty_question_view(request):
    return render(request, 'quiz/faculty_question.html')


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_add_question_view(request):
    questionForm = QFORM.QuestionForm()
    if request.method == 'POST':
        questionForm = QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            course = QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course = course
            question.save()

        else:
            print("form is invalid")
        return HttpResponseRedirect('/question/faculty-view-question')

    return render(request, 'quiz/faculty_add_question.html', {'questionForm': questionForm})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_view_question_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'quiz/faculty_view_question.html', {'courses': courses})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def see_question_view(request, pk):
    questions = QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request, 'question/see_question.html', {'questions': questions})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def remove_question_view(request, pk):
    question = QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/question/faculty-view-question')


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_view_exam(request):
    return render(request, 'quiz/faculty_exam.html')


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_add_exam_view(request):
    courseForm = QFORM.CourseForm()
    if request.method == 'POST':
        courseForm = QFORM.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/question/faculty-view-exam')
    return render(request,'quiz/faculty-add-exam.html', {'courseForm': courseForm})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_view_exam(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'quiz/faculty_view_exam.html', {'courses': courses})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def delete_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/question/faculty-view-exam')


#@login_required(login_url='faculty/login')
def faculty_question_view(request):
    return render(request, 'quiz/faculty_question.html')


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_add_question_view(request):
    questionForm = QFORM.QuestionForm()
    if request.method == 'POST':
        questionForm = QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            course = QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course = course
            question.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/question/faculty-view-question')
    return render(request, 'quiz/faculty_add_question.html', {'questionForm': questionForm})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def faculty_view_question_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'quiz/faculty_view_question.html', {'courses': courses})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def see_question_view(request, pk):
    questions = QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request, 'quiz/see_question.html', {'questions': questions})


#@login_required(login_url='faculty/login')
#@user_passes_test(is_faculty)
def remove_question_view(request, pk):
    question = QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/question/faculty-view-question')

