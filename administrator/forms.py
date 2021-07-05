from django import forms
from django.contrib.auth.models import User

from .models import (
    Administrator,
    Institute
)


def create_attributes(placeholder='', classes=[]):
    attrs = {'placeholder': placeholder, 'class': 'un'}
    attrs['class'] += ' '.join(classes)
    attrs['align'] = 'center'
    return attrs


# 'class': 'form-control'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    **create_attributes(
                        placeholder='Username',
                    ),
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    **create_attributes(
                        placeholder='Password',
                    ),
                }
            )
        }


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    **create_attributes(
                        placeholder='Institute name',
                    ),
                }
            ),

            'code': forms.NumberInput(
                attrs={
                    'min': 1,
                    **create_attributes(
                        placeholder='Institute code',
                    ),
                }
            ),

            'city': forms.TextInput(
                attrs={
                    **create_attributes(
                        placeholder='City',
                    ),
                }
            ),

            'state': forms.TextInput(
                attrs={
                    **create_attributes(
                        placeholder='State',
                    ),
                }
            ),

            'country': forms.TextInput(
                attrs={
                    **create_attributes(
                        placeholder='Country',
                    ),
                }
            ),

            'website_url': forms.URLInput(
                attrs={
                    **create_attributes(
                        placeholder='Website URL',
                    ),
                }
            ),
        }


class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    **create_attributes(
                        placeholder='Email',
                    ),
                }
            )
        }
