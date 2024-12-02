from django.shortcuts import render, get_object_or_404
from gestorProducto.models import *
from gestorProducto.forms import CategoriaRegistrationForm , ProductoRegistrationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import DatabaseError
from django.core.exceptions import ValidationError






def buscar_productos(request):
    query = request.GET.get('q')
    productos = Producto.objects.all()
    try:
        if query:
            productos = productos.filter(nombre__icontains=query) | productos.filter(ubicacion__icontains=query) | productos.filter(usuario__username__icontains=query)
    except DatabaseError as e:
        print(f"Error al acceder a la base de datos: {e}")
        productos = []
    return render(request, 'searchproductos.html', {'productos': productos, 'query': query})


def productoData(request):
    producto=Producto.objects.all()
    data={'producto':producto}
    return render(request,'tablas/tabla_producto.html',data)

@login_required(login_url='login')  
def registrarProducto(request):
    form = ProductoRegistrationForm()
    
    if request.method == 'POST':
        form = ProductoRegistrationForm(request.POST, files=request.FILES)
        
        if form.is_valid():
            try:
                producto = form.save(commit=False)
                producto.usuario = request.user
                print("El formulario es valido")
                producto.save()
                return HttpResponseRedirect(reverse("ver_producto"))
            except ValidationError as e:
                form.add_error(None, f"Error al guardar el producto: {e}")
            except Exception as e:
                form.add_error(None, f"Ha ocurrido un error: {e}")
                
    data = {'form': form}
    return render(request, 'forms/form_producto.html', data)

@login_required(login_url='login')  
def registrarCategoria(request):
    user = request.user
    if request.user.is_staff:
        form = CategoriaRegistrationForm()
        if request.method=='POST':
            form = CategoriaRegistrationForm(request.POST)
            if form.is_valid():
                print("El formulario es valido")
                form.save()
                return HttpResponseRedirect(reverse("ver_categorias"))
        data = {'form' : form }
        return render (request,'forms/form_categoria.html',data)
    else:
        return render (request, 'index.html')


@login_required(login_url='login')
def categoriaData(request):
    categoria = Categoria.objects.all()
    if request.user.is_staff:
        data = {'categoria': categoria}
        return render(request, 'tablas/tabla_categoria.html', data)
    else:
        return render(request, 'index.html')

@login_required(login_url='login')  
def editarCategoria(request,id ):
    user = request.user
    if request.user.is_staff:
        categoria=Categoria.objects.get(id = id )
        form=CategoriaRegistrationForm(instance=categoria)
        if (request.method=='POST'):
            form=CategoriaRegistrationForm(request.POST,instance=categoria)
            if form.is_valid():
                    form.save()
            return  HttpResponseRedirect(reverse("ver_categorias"))
        data = {'form' : form } 
        return render (request, 'forms/form_categoria.html',data)
    else:
        return render (request, 'index.html')


@login_required(login_url='login')     
def eliminarCategoria(request,id):
    categoria=Categoria.objects.get(id = id )
    if request.user.is_staff:
        categoria.delete()
        return  HttpResponseRedirect(reverse("ver_categorias"))
    else:
        return render (request, 'index.html')



@login_required(login_url='login')  
def editarProducto(request,id ):
    producto=Producto.objects.get(id = id )
    form=ProductoRegistrationForm(instance=producto, files=request.FILES)
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




