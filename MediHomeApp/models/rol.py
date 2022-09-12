from django.db import models

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion_rol = models.CharField(max_length=1)