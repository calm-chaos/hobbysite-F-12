from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegistrationForm(UserCreationForm):
    display_name = forms.CharField(max_length=63)
    email_address = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "display_name", "email_address"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["display_name", "email_address"]
