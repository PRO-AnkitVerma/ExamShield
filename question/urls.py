"""Faculty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [

    path('faculty-question/', views.faculty_question, name='faculty-question'),
    path('faculty-add-question/', views.faculty_add_question, name='faculty-add-question'),
    path('faculty-view-question/', views.faculty_view_question, name='faculty-view-question'),
    path('see-question/', views.see_question, name='see-question'),
    path('faculty-add-exam/', views.faculty_add_exam, name='faculty-add-exam'),
    path('faculty-view-exam/', views.faculty_view_exam, name='faculty-view-exam'),
    path('faculty-exam/', views.faculty_exam, name='faculty-exam'),
]
