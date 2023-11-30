from django.shortcuts import render
from gestorProducto.models import *
from gestorProducto.forms import CategoriaRegistrationForm , ProductoRegistrationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def productoData(request):
    producto=Producto.objects.all()
    data={'producto':producto}
    return render(request,'tablas/tabla_producto.html',data)

def registrarProducto(request):
    form=ProductoRegistrationForm()
    if request.method=='POST':
        form=ProductoRegistrationForm(request.POST)
        if form.is_valid():
            producto=form.save(commit=False)
            producto.usuario=request.user
            print("El formulario es valido")
            producto.save()
            return HttpResponseRedirect(reverse("ver_producto"))
    data = {'form':form}
    return render(request,'forms/form_producto.html',data)

@login_required(login_url='login')  
def registrarCategoria(request):
    user = request.user
    form = CategoriaRegistrationForm()
    if request.method=='POST':
        form = CategoriaRegistrationForm(request.POST)
        if form.is_valid():
            print("El formulario es valido")
            form.save()
            return HttpResponseRedirect(reverse("ver_categorias"))
    data = {'form' : form }
    return render (request,'forms/form_categoria.html',data)


@login_required(login_url='login')  
def categoriaData(request):
    categoria = Categoria.objects.all()
    data = {'categoria': categoria}
    return render(request,'tablas/tabla_categoria.html',data)

@login_required(login_url='login')  
def editarCategoria(request,id ):
    user = request.user
    categoria=Categoria.objects.get(id = id )
    form=CategoriaRegistrationForm(instance=categoria)
    if (request.method=='POST'):
        form=CategoriaRegistrationForm(request.POST,instance=categoria)
        if form.is_valid():
                form.save()
        return  HttpResponseRedirect(reverse("ver_categorias"))
    data = {'form' : form } 
    return render (request, 'forms/form_categoria.html',data)



@login_required(login_url='login')     
def eliminarCategoria(request,id):
    categoria=Categoria.objects.get(id = id )
    categoria.delete()
    return  HttpResponseRedirect(reverse("ver_categorias"))



@login_required(login_url='login')  
def editarProducto(request,id ):
    producto=Producto.objects.get(id = id )
    form=ProductoRegistrationForm(instance=producto)
    if (request.method=='POST'):
        form=ProductoRegistrationForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
        return  HttpResponseRedirect(reverse("ver_producto"))
    data = {'form' : form } 
    return render (request, 'forms/form_producto.html',data)






@login_required(login_url='login')  
def eliminarProducto(request,id):
    user = request.user
    producto=Producto.objects.get(id = id )
    producto.delete()
    return  HttpResponseRedirect(reverse("ver_producto"))

