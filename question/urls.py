from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('faculty-exam', views.faculty_exam_view,name='faculty-exam'),
    path('faculty-add-exam/', views.faculty_add_exam_view, name='faculty-add-exam'),
    path('faculty-view-exam/', views.faculty_view_exam_view, name='faculty-view-exam'),
    path('delete-exam/<int:pk>', views.delete_exam_view,name='faculty-exam'),
    path('faculty-question/', views.faculty_question_view,name='faculty-question'),
    path('faculty-add-question', views.faculty_add_question_view,name='faculty-add-question'),
    path('faculty-view-question', views.faculty_view_question_view,name='faculty-view-question'),
    path('see-question/<int:pk>', views.see_question_view,name='see-question'),
    path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
]