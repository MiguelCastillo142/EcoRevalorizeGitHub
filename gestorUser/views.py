from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from gestorProducto.models import *
from .forms import SignUpForm
from django.contrib.auth.models import User

@login_required(login_url='login')
def editarUsuario(request, id):
    usuario = request.user
    if usuario.is_staff:
        user_to_edit = User.objects.get(id=id)
        form = SignUpForm(instance=user_to_edit)
        
        if request.method == 'POST':
            form = SignUpForm(request.POST, instance=user_to_edit)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("ver_usuarios"))
        
        data = {'form': form}
        return render(request, 'forms/info.html', data)
    else:
        return render(request, 'index.html')
def usuariodata(request):
    usuario = Usuario.objects.all()
    if request.user.is_staff:
        data = {'usuarios': usuario}
        return render(request, 'tablas/tabla_usuario.html', data)
    else:
        return render(request, 'index.html')

def signUp(request):
    usuario=Usuario
    form=SignUpForm
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print(request,"Te registraste correctamente")
            return redirect('/')
    return render(request,'forms/signUp.html',{'form':form})
    
@login_required(login_url='login')  
def postlogin(request):
    user = request.user
    return render(request,'bases/interfaz.html')


def listaproducto(request):
    producto = Producto.objects.all()
    data = {'producto': producto}
    return render(request, 'vistaproductos.html', data)