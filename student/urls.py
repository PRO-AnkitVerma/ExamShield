"""Student URL Configuration

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
from django.shortcuts import redirect
from . import views

app_name = 'student'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    # path('', views.login, redirect('student:login')),
    # TODO: add redirect for '' to login
    path('dashboard/', views.student_dashboard_view, name='dashboard'),
    path('view-result', views.view_result_view,name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
    path('student-marks', views.student_marks_view,name='student-marks'),
    path('start-exam/<int:pk>/', views.start_exam_view,name='start-exam'),
    path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
    path('student-exam', views.student_exam_view,name='student-exam'),
    path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
]
