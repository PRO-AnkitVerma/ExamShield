from django.http import HttpResponse
from django.shortcuts import render

from mysite.decorators import allowed_users


@allowed_users(allowed_groups=['faculty'])
def create_assignment(request):
    if request.method == 'GET':
        return HttpResponse('Create Assignment Page')

    if request.method == 'POST':
        return HttpResponse('Validating Creation of Assignment')


    return render(request, 'assignment/create-assignment.html')
