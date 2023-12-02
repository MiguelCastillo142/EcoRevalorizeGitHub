from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
            return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
    contacto=models.CharField(max_length=30)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE) 
    def __str__(self):
        return self.nombre
    
