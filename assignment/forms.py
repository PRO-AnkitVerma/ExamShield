from django import forms

from assignment.models import Assignment, AssignmentInstance


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['no', 'question', 'total_marks', 'deadline']


class AssignmentInstanceForm(forms.ModelForm):
    class Meta:
        model = AssignmentInstance
        fields = ['file_uploaded']
