from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from gestorUser.views  import *
from gestorProducto.views import *
from django.views.generic.base import TemplateView
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/',include("django.contrib.auth.urls"),name='login'),
    path('signUp/',signUp,name="signUp"),
    path('interfaz/',postlogin,name="board"),
     
    path('addproducto/',registrarProducto,name="insertar_producto"),
    path('productos/',productoData,name="ver_producto"),

    path('editarusuario/<int:id>', editarUsuario, name="editarusuario"),
    path('usuariodata/', usuariodata, name="usuariodata"),

    path('addcategoria/',registrarCategoria,name="agregar_categoria"),
    path('categorias/',categoriaData,name="ver_categorias"),

    path('editarcategoria/<int:id>', editarCategoria, name="editarcategoria"),
    path('eliminarcategoria/<int:id>', eliminarCategoria, name="eliminarcategoria"),

    path('editarproducto/<int:id>',editarProducto, name="editarproducto"),
    path('eliminarproducto/<int:id>', eliminarProducto, name="eliminarproducto"),
    
    path('',TemplateView.as_view(template_name="index.html"),name='index'),
    path('lista/',listaproducto,name="productos"),
    path('search/',buscar_productos,name="search"),
    
    path('editarnombre/', editar_nombre, name='editar_nombre'),

 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
