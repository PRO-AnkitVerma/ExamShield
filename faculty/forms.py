from django import forms

from utils.form_helper import create_attributes
from .models import faculty as Faculty


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
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
