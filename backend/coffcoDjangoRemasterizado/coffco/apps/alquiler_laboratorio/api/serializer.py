from rest_framework import serializers
from apps.alquiler_laboratorio.models import AlquilerLaboratorio
from apps.users.models import User

class alquiler_Serializer(serializers.ModelSerializer):
    fk_usuarios = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = AlquilerLaboratorio
        fields = ['fecha_alquiler', 'fk_usuarios', 'estado', 'fecha_fin']
    