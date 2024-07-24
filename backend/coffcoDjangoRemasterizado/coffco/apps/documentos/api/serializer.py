from rest_framework import serializers
from apps.documentos.models import Documentos
from apps.users.models import User


class documentos_Serializer(serializers.ModelSerializer):
    fk_id_usuarios = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Documentos
        fields = ['nombre', 'fecha_carga', 'fk_id_usuarios', 'descripcion', 'formato', 'estado']
