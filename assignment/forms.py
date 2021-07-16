from django import forms

from assignment.models import Assignment, AssignmentInstance
from utils.form_helper import create_attributes


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['no', 'question', 'total_marks', 'deadline', 'reference']
        labels = {
            'no': 'Assignment No',
            'question': 'Assignment Title',
        }
        widgets = {
            'no': forms.NumberInput(
                attrs={
                    **create_attributes(
                        placeholder='Assignment No',
                    ),
                }
            ),

            'question': forms.TextInput(
                attrs={
                    **create_attributes(
                        placeholder='Assignment Title',
                    )
                }
            ),

            'deadline': forms.TextInput(
                attrs={
                    **create_attributes(
                        placeholder='Deadline',
                    )
                }
            ),

            'total_marks': forms.NumberInput(
                attrs={
                    **create_attributes(
                        placeholder='Total Marks',
                    ),
                }
            )
        }


class AssignmentInstanceForm(forms.ModelForm):
    class Meta:
        model = AssignmentInstance
        fields = ['file_uploaded']
