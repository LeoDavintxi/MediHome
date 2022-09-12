from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'descripcion_rol']