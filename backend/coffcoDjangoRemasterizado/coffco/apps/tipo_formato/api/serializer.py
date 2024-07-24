from rest_framework import serializers
from apps.tipo_formato.models import TipoFormato

class tipo_formato_Serializer(serializers.ModelSerializer):

    class Meta:
        model = TipoFormato
        fields = ['nombre']
