from rest_framework import serializers
from MediHomeApp.models.rol import Rol

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'user_name','Rol', 'password', 'nombre', 'apellido', 'direccion', 'correo', 'activo']