from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O endereço de e-mail é obrigatório.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(null=True, blank=True, max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    numero_telefone = models.CharField(null=True, blank=True, max_length=15)
    rua = models.CharField(null=True, blank=True, max_length=100)
    numero = models.CharField(null=True, blank=True, max_length=10)
    complemento = models.CharField(null=True, blank=True, max_length=100)
    bairro = models.CharField(null=True, blank=True, max_length=100)
    cep = models.CharField(null=True, blank=True, max_length=10)
    cidade = models.CharField(null=True, blank=True, max_length=100)
    estado = models.CharField(null=True, blank=True, max_length=2)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # torna e-mail o campo de login
    REQUIRED_FIELDS = []  # caso precise de campos adicionais p registrar usuario

    def __str__(self):
        return self.email
