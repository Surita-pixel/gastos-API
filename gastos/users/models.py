from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager

from django.dispatch import receiver


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password=None, username='admin', email='admin@example.com'):
        user = self.model(username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user



class Usuario(AbstractBaseUser):
    usuario_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(verbose_name='email', unique=False, max_length=250)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]

    objects = MyUserManager()

    def save(self, *args, **kwargs):
        # Filtra la base de datos en busca de registros con userio_id igual al de la instancia actual
        existing_users = Usuario.objects.filter(usuario_id=self.usuario_id)
        if existing_users:
            # Si existe al menos un registro con userio_id igual, se le suma 1 al valor del userio_id
            self.userio_id += 1
        # Guarda el registro en la base de datos
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

@receiver(post_save, sender=Usuario)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    
    
@receiver(post_save, sender=Usuario)
def save_profile(sender, instance, **kwargs):
    instance.perfil.save()

@receiver(post_save, sender=Usuario)
def update_user_profile(sender, instance, created, **kwargs):
    """
    Signals the Profile about User creation.
    """
    if created:
        Perfil.objects.create(usuario=instance)
    instance.perfil.save()