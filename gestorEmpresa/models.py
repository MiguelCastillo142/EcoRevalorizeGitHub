from django.db import models
# Se crea un modelo para tipo empresa es como una categoria 
class Tipoempresa(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
            return self.nombre
    
class Empresa(models.Model):
    rutempresa = models.CharField(max_length=14)
    nombre= models.CharField(max_length=30)
    correo=models.CharField(max_length=30)
    telefono=models.CharField(max_length=13)
    tipoempresa=models.ForeignKey(Tipoempresa,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
