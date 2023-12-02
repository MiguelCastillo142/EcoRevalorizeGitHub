from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(models.Model):
    rut=models.CharField(max_length=20)
    usuario =models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.username
    
@receiver(post_save, sender= User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)
        
@receiver(post_save, sender = User)
def guardar_usuario(sender, instance, created, **kwargs):
    instance.usuario.save()
