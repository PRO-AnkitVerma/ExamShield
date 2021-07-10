from django.contrib.admin import models
from django.contrib.auth.models import User
from django.forms import forms


class StudentUserForm(forms.ModelForm):
        class Meta:
                model=User
                fields=['first_name','last_name','userid']

