from cProfile import label
from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from shortener.models import *

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=False, help_text="Optional", label="name")
    username = forms.CharField(max_length=20, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address")

    class Meta:
        model = Users
        field = (
            "username",
            "full_name",
            "email",
            "password1",
            "password2",
        )