from rest_framework import serializers
from apps.datos.models import Datos
from apps.versiones.models import Versiones

class datos_Serializer(serializers.ModelSerializer):
    fk_id_formato = serializers.PrimaryKeyRelatedField(queryset=Versiones.objects.all())

    class Meta:
        model = Datos
        fields = ['nombre', 'tipo', 'estado', 'fk_id_formato']
