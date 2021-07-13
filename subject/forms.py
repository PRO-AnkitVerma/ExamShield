from django import forms
from subject.models import Subject
from utils.form_helper import create_attributes


class SubjectForm(forms.ModelForm):
        class Meta:
            model = Subject
            fields = [
                'code',
                'name',

            ]