from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario

class SignUpForm(UserCreationForm):
    first_name =forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email= forms.EmailField(required=False)
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')