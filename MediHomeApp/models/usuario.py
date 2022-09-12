import this
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .rol import Rol


class UserManager(BaseUserManager):
    def create_user(self, user_name, password=None):
        if not user_name:
            raise ValueError('Users must have an username')
        user = self.model(username=user_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password):
        user = self.create_user(
            user_name=user_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=15)
    password = models.CharField(max_length=256)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    correo = models.EmailField(max_length=20)
    create_date = models.DateField()
    activo = models.BooleanField()
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    id_registro = models.ForeignKey('self', on_delete=models.CASCADE)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'user_name'
