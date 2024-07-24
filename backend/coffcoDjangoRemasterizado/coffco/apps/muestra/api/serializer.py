from rest_framework import serializers
from apps.muestra.models import Muestra
from apps.finca.models import Finca


class muestra_Serializer(serializers.ModelSerializer):
    fk_id_finca = serializers.PrimaryKeyRelatedField(queryset=Finca.objects.all())
    class Meta:
        model = Muestra
        fields = ['cantidad', 'fk_id_finca', 'fecha_muestra']
