from django.contrib import auth, messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from question.forms import ResultForm
from mysite.decorators import allowed_users
from question import models as QMODEL
from student import models


class Login(View):
    def get(self, request):
        return render(request, 'student/login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user and user.groups.filter(name='student'):
                auth.login(request, user)
                return redirect('student:dashboard')
            else:
                messages.error(request, 'Error: Invalid Credentials!')
                return render(request, 'student/login.html')

        messages.warning(request, 'Please enter credentials to login')
        return render(request, 'student/login.html')


@login_required(login_url='student:login')
def logout(request):
    auth.logout(request)
    return redirect('student:login')


def is_student(user):
    # TODO: ask about this group!
    return user.groups.filter(name='STUDENT').exists()


def student_dashboard_view(request):
    dict = {

        'total_course': QMODEL.Course.objects.all().count(),
        'total_question': QMODEL.Question.objects.all().count(),
    }
    # return HttpResponse('Hello')
    return render(request, 'student/dashboard.html')
    # return render(request, 'student/dashboard.html', context=dict)


# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
def view_result_view(request):
    resultForm = ResultForm(request.POST)
    if resultForm.is_valid():
        resultForm.save()
    else:
        print("form is invalid")

    courses = QMODEL.Course.objects.all()
    # totalmarks.courses.save()
    return render(request, 'student/view-result.html', {'courses': courses})


# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
def check_marks_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    student = models.student.objects.get(user_id=request.user.id)
    results = QMODEL.Result.objects.all().filter(exam=course).filter(student=student)

    return render(request, 'student/check-marks.html', {'results': results})


# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
def student_marks_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'student/student-marks.html', {'courses': courses})


# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
# @csrf_exempt
def start_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    questions = QMODEL.Question.objects.all().filter(course=course)
    total_questions = questions.count()
    if request.method == 'POST':
        pass
    response = render(request, 'student/start-exam.html',
                      {'course': course, 'questions': questions, 'total_questions': total_questions})
    response = render(request, 'student/start-exam.html',
                      {'course': course, 'questions': questions, 'total_questions': total_questions})
    response.set_cookie('course_id', course.id)
    return response


# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
def take_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    total_questions = QMODEL.Question.objects.all().filter(course=course).count()
    questions = QMODEL.Question.objects.all().filter(course=course)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks

    return render(request, 'student/take-exam.html',
                  {'course': course, 'total_questions': total_questions, 'total_marks': total_marks})


# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
def student_exam_view(request):
    courses = QMODEL.Course.objects.filter()
    return render(request, 'student/student-exam.html', {'courses': courses})


# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = QMODEL.Course.objects.get(id=course_id)

        total_marks = 0
        questions = QMODEL.Question.objects.all().filter(course=course)
        for i in range(len(questions)):

            selected_ans = request.COOKIES.get(str(i + 1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = models.student.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks = total_marks
        result.exam = course
        result.student = student
        result.save()

        return HttpResponseRedirect('view-result')




# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
def student_marks_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'student/student_marks.html', {'courses': courses})


@allowed_users(allowed_groups=['student'])
def dashboard(request):
    return render(request, 'student/dashboard.html')
