from rest_framework import serializers
from apps.servicios.models import Servicios
from apps.muestra.models import Muestra
from apps.versiones.models import Versiones

class servicios_Serializer(serializers.ModelSerializer):
    fk_id_muestra = serializers.PrimaryKeyRelatedField(queryset=Muestra.objects.all())
    fk_formato = serializers.PrimaryKeyRelatedField(queryset=Versiones.objects.all())

    class Meta:
        model = Servicios
        fields = ['tipo_servicios', 'fk_id_muestra', 'fk_formato']
