from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth.forms import UserChangeForm


class SignUpForm(UserCreationForm):
    rut =forms.CharField(max_length=140, required=True)
    email= forms.EmailField(required=False)
    class Meta:
        model=User
        fields=('username','rut','email','password1','password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Ingresa el nombre actual'
        self.fields['username'].help_text = 'Requerido. 150 caracteres como máximo. Únicamente letras, dígitos y @/./+/-/_'


class EditarNombreForm(UserChangeForm):
    password = None 
    class Meta:
        model = User
        fields = ['username', 'first_name']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Ingresa el nombre actual'
        self.fields['username'].help_text = 'Requerido. 150 caracteres como máximo. Únicamente letras, dígitos y @/./+/-/_'
        self.fields['first_name'].label = 'Ingresa un nuevo nombre personal'
        self.fields['first_name'].help_text = 'Requerido. 150 caracteres como máximo. Únicamente letras, dígitos y @/./+/-/_'