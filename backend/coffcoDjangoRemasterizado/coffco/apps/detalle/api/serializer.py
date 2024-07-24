from rest_framework import serializers
from apps.detalle.models import Detalle
from apps.versiones.models import Versiones
from apps.datos.models import Datos
from apps.servicios.models import Servicios

class detalle_Serializer(serializers.ModelSerializer):
    fk_id_formato = serializers.PrimaryKeyRelatedField(queryset=Versiones.objects.all())
    fk_id_datos = serializers.PrimaryKeyRelatedField(queryset=Datos.objects.all())
    fk_id_servicios = serializers.PrimaryKeyRelatedField(queryset=Servicios.objects.all())
    class Meta:
        model = Detalle
        fields = ['fk_id_formato', 'fk_id_datos', 'valor', 'fk_id_servicios']
