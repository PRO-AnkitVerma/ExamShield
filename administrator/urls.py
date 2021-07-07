"""Administrator URL Configuration

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
from django.views.generic import RedirectView

from . import views

app_name = 'administrator'

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=False), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.Register.as_view(), name='register'),
    path('create-faculty/', views.create_faculty, name='create-faculty'),
    path('create-student/', views.create_student, name='create-student'),
    path('edit-institute-profile/', views.edit_institute_profile, name='edit-institute-profile'),
]
