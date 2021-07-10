from django import forms

from utils.form_helper import create_attributes
from .models import student as Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'enroll_no']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    **create_attributes(
                        placeholder='Email',
                    ),
                }
            ),

            'enroll_no': forms.NumberInput(
                attrs={
                    **create_attributes(
                        placeholder='Enrollment no',
                    ),
                }
            )
        }
