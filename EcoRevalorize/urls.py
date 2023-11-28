from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from gestorEmpresa  import views
from gestorUser  import views
from gestorProducto import views
from django.views.generic.base import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/',include("django.contrib.auth.urls"),name='login'),
    path('',TemplateView.as_view(template_name="index.html"),name='index'),
]
