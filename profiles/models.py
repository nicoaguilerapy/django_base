from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email

class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, blank = True, null = True)
    first_name = models.CharField('Nombres', max_length = 200, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 220, blank = True, null = True)
    phone = models.CharField('Número de Celular', max_length = 25, blank = True, null = True)
    active = models.BooleanField('Activado', default= True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-last_name']
    
    def __str__(self):
        return "{}, {}".format(self.first_name, self.last_name)


@receiver(post_save, sender=CustomUser)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        new_profile, created = Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")