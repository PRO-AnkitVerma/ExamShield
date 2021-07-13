"""Assignment URL Configuration

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
from . import views, api

app_name = 'assignment'

urlpatterns = [
    # faculty operations
    path('create-assignment/', views.create_assignment, name='create-assignment'),
    path('review-assignment-instance/<int:assignment_instance_id>/', views.review_assignment_instance,
         name='review-assignment-instance'),
    path('faculty-view-assignments/', views.faculty_view_all_given_assignments, name='faculty-view-assignments'),
    path('faculty-view-assignment-instances/<int:assignment_id>/', views.faculty_view_all_assignment_instances,
         name='faculty-view-assignment-instances'),

    # student operations
    path('submit-assignment/<int:assignment_id>/', views.submit_assignment_instance, name='submit-assignment'),
    path('student-view-assignments/', views.student_view_all_given_assignments, name='student-view-assignments'),
    path('student-view-all-returned-assignment-instances/', views.student_view_all_returned_assignment_instances,
         name='student-view-all-returned-assignment-instances'),

    # api urls
    path('api/get-all-assignments/student:<int:student_enroll_no>/', api.get_all_assignments,
         name='get-all-assignments'),
    path('api/get-all-assignments/student:<int:student_enroll_no>/subject:<int:subject_id>/',
         api.get_all_assignments,
         name='get-all-assignments'),
]
