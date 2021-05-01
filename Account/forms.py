from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required, add a valid email")

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'phone')


