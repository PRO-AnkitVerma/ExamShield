from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from assignment.forms import AssignmentForm
from assignment.models import Assignment
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
    assignment = get_object_or_404(Assignment, id=pk)
    context = {
        'assignment': assignment,
    }
    return render(request, 'assignment/evaluate-assignment.html', context=context)
