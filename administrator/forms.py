from django import forms
from django.contrib.auth.models import User

from .models import (
    Administrator,
    Institute
)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'id': 'usernamefield', 'class': 'form-control',
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    'id': 'passwordfield', 'class': 'form-control',
                }
            )
        }


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = '__all__'


class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['email']
