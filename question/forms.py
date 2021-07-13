from django import forms
from question.models import Course, Question
from subject.models import Subject


class CourseForm(forms.ModelForm):
    subjectID = forms.ModelChoiceField(queryset=Subject.objects.all(), empty_label="subject Name",
                                       to_field_name="id")
    class Meta:
        model=Course
        fields=['course_name','question_number','total_marks']


class QuestionForm(forms.ModelForm):
    # this will show dropdown __str__ method course model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label="Course Name",
                                      to_field_name="id")

    class Meta:
        model = Question
        fields = ['marks', 'question', 'option1', 'option2', 'option3', 'option4', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }

