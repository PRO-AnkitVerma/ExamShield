from django.shortcuts import render, HttpResponse
from mysite.models import Contact


# Create your views here.
def home(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'mysite/home.html')
