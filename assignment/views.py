from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from assignment.forms import AssignmentForm, AssignmentInstanceForm
from assignment.models import Assignment, AssignmentInstance
from mysite.decorators import allowed_users
from subject.models import Subject


@allowed_users(allowed_groups=['faculty'])
def create_assignment(request):
    subjects = Subject.objects.filter(faculty=request.user.faculty)

    if request.method == 'GET':
        context = {
            'subjects': subjects,
            'assignment_form': AssignmentForm(),
        }
        return render(request, 'assignment/create-assignment.html', context=context)

    if request.method == 'POST':
        assignment_form = AssignmentForm(data=request.POST)
        subject_id = request.POST.get('subject', '')

        # data is valid then save the assignment
        if subject_id and assignment_form.is_valid():
            assignment = assignment_form.save(commit=False)
            assignment.subject = Subject.objects.get(id=subject_id)
            assignment.save()
            messages.success(request, 'Assignment Created!')

            context = {
                'subjects': subjects,
                'assignment_form': AssignmentForm(),
            }
            return render(request, 'assignment/create-assignment.html', context=context)

        # data validation failed!
        context = {
            'subjects': subjects,
            'assignment_form': assignment_form,
        }
        messages.error(request, f'''
        {assignment_form.errors.as_text()}
        ''')
        return render(request, 'assignment/create-assignment.html', context=context)

    # other methods than Get or Post not allowed
    return HttpResponse('BAD REQUEST')


@allowed_users(allowed_groups=['faculty'])
def review_assignment(request):
    assignments = Assignment.objects.filter(subject__in=Subject.objects.filter(faculty=request.user.faculty))
    context = {'assignments': assignments, }
    print(assignments)
    return render(request, 'assignment/review-assignment.html', context=context)


@allowed_users(allowed_groups=['faculty'])
def evaluate_assignment(request, pk):
    # TODO: to finish after creating assignment instances!
    assignment = get_object_or_404(Assignment, id=pk)

    if request.method == 'GET':
        context = {
            'assignment': assignment,
        }
        return render(request, 'assignment/evaluate-assignment.html', context=context)


@allowed_users(allowed_groups=['student'])
def submit_assignment_instance(request):
    student = request.user.student
    if request.method == 'GET':
        context = {
            'assignments': Assignment.objects.filter(subject__in=student.subjects.all()),
        }
        return render(request, 'assignment/submit-assignment.html', context=context)

    if request.method == 'POST':
        context = {

        }
        return render(request, 'assignment/submit-assignment.html', context=context)

    return HttpResponse('BAD REQUEST')


@allowed_users(allowed_groups=['student'])
def student_view_all_given_assignments(request):
    return HttpResponse('View Assignments')


def view_assignment_instance(request, assignment_instance_no):
    return HttpResponse('Viewing submitted AssignmentInstance')
