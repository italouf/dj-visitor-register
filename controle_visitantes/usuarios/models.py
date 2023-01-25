from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin,)

class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None):
        usuario = self.model(email=self.normalize_email(email))

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)
        
        usuario.save()
        return usuario

    def create_superuser(self, email, password=None):
        usuario = self.create_user(email=self.normalize_email(email), password=password,)

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)
        usuario.save()

        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name=("Email"), max_length= 128, unique=True)

    is_active = models.BooleanField(verbose_name=("Ativo"), default=True)

    is_staff = models.BooleanField(verbose_name=("Equipe de gerenciamento"), default=False)

    is_superuser = models.BooleanField(verbose_name=("Super usuário"), default=False)

    USERNAME_FIELD = "email"

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"
    
    def __str__(self):
        return self.email