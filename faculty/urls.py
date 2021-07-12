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

app_name = 'faculty'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    # TODO: add redirect for '' to login
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # path('faculty-exam', views.faculty_exam_view, name='faculty-exam'),
    # path('faculty-add-exam', views.faculty_add_exam_view, name='faculty-add-exam'),
    # path('faculty-view-exam', views.faculty_view_exam_view, name='faculty-view-exam'),
    # path('delete-exam/<int:pk>', views.delete_exam_view, name='faculty-exam'),
    #
    # path('faculty-question', views.faculty_question_view, name='faculty-question'),
    # path('faculty-add-question', views.faculty_add_question_view, name='faculty-add-question'),
    # path('faculty-view-question', views.faculty_view_question_view, name='faculty-view-question'),
    # path('see-question/<int:pk>', views.see_question_view, name='see-question'),
    # path('remove-question/<int:pk>', views.remove_question_view, name='remove-question'),

]
