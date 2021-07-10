from django import forms

from assignment.models import Assignment, AssignmentInstance


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['no', 'question', 'total_marks', 'assigned_date']


class AssignmentInstanceForm(forms.ModelForm):
    class Meta:
        model = AssignmentInstance
        fields = ['file_uploaded']
