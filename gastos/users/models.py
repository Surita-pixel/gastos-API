from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractBaseUser, User

from django.dispatch import receiver


# Create your models here.
class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', unique=True, max_length=250)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['__all__']
    # 
    # gasto = models.OneT

    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kawargs):
    instance.perfil.save()