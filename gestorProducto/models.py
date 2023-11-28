from django.db import models

# 
class Categoria(models.Model):
    nombre =models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion= models.CharField(max_length=30)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
