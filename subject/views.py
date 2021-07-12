from django.shortcuts import render, HttpResponse

def add_subject(request):


    return render(request, 'faculty/add-subject.html')
