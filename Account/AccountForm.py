from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.forms import ValidationError


class RegistrationForm(ModelForm):
    re_password = forms.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password', 're_password']

    def clean_email(self):
        email = self.cleaned_data['email']
        return email



