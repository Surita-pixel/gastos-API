from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(
                                User, 
                                on_delete=models.CASCADE,
                                )
    bio = models.CharField(
                            max_length=250, 
                            blank=True,
                            )
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwarg):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()