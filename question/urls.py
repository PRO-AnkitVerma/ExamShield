from django.urls import path

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
from . import views, api

app_name = 'question'

urlpatterns = [
    # exam urls
    path('faculty-exam/', views.faculty_exam_view, name='faculty-exam'),
    path('question/faculty-add-exam/', views.faculty_add_exam_view, name='faculty-add-exam'),
    path('faculty-view-exam/', views.faculty_view_exam_view, name='faculty-view-exam'),
    path('delete-exam/<int:pk>/', views.delete_exam_view, name='faculty-delete-exam'),

    # question urls
    path('faculty-question/', views.faculty_question_view, name='faculty-question'),
    path('faculty-add-question/', views.faculty_add_question_view, name='faculty-add-question'),
    path('faculty-view-question/', views.faculty_view_question_view, name='faculty-view-question'),
    path('see-question/<int:pk>/', views.see_question_view, name='see-question'),
    path('remove-question/<int:pk>/', views.remove_question_view, name='remove-question'),

    # api urls
    path('api/get-course/<int:course_id>/', api.get_course, name='get-course'),
    path('api/get-all-questions/<int:course_id>/', api.get_all_questions, name='get-all-questions'),
]
