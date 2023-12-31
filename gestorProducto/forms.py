from django import forms
from gestorProducto.models import *
from gestorProducto import models


class ProductoRegistrationForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    contacto=forms.CharField()
    ubicacion=forms.CharField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    imagen = forms.ImageField(required=False)


    nombre.widget.attrs['class']='form-control'
    descripcion.widget.attrs['class']='form-control'
    contacto.widget.attrs['class']='form-control'
    ubicacion.widget.attrs['class']='form-control'
    categoria.widget.attrs['class']='form-control'
    imagen.widget.attrs['class'] = 'form-control'

    class Meta:
        model=Producto
        exclude = ['usuario']
        fields='__all__'

class ProductoRegistrationForm(forms.ModelForm):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    contacto=forms.CharField()
    ubicacion=forms.CharField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    imagen = forms.ImageField(required=False)

    nombre.widget.attrs['class']='form-control'
    descripcion.widget.attrs['class']='form-control'
    contacto.widget.attrs['class']='form-control'
    ubicacion.widget.attrs['class']='form-control'
    categoria.widget.attrs['class']='form-control'
    imagen.widget.attrs['class'] = 'form-control'
    class Meta:
        model=Producto
        exclude = ['usuario']
        fields='__all__'

class CategoriaRegistrationForm(forms.Form):
    nombre = forms.CharField()
    nombre.widget.attrs['class']='form-control'
    class Meta:
        model=Categoria
        fields='__all__'

class CategoriaRegistrationForm(forms.ModelForm):
    nombre = forms.CharField()
    nombre.widget.attrs['class']='form-control'
    class Meta:
        model=Categoria
        fields='__all__'
