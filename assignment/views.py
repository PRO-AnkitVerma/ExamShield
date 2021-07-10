from django.http import HttpResponse
from django.shortcuts import render

from mysite.decorators import allowed_users


@allowed_users(allowed_groups=['faculty'])
def create_assignment(request):
    return render(request, 'assignment/create-assignment.html')

@allowed_users(allowed_groups=['faculty'])
def create_assignment(request):
    return render(request, 'assignment/submit-assignment.html')
