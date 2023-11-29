from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario

class SignUpForm(UserCreationForm):
    rut =forms.CharField(max_length=140, required=True)
    email= forms.EmailField(required=False)
    class Meta:
        model=User
        fields=('username','rut','email','password1','password2')