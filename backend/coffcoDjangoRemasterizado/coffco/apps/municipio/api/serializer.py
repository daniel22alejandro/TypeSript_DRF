from rest_framework import serializers
from apps.municipio.models import Municipio

class municipio_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Municipio
        fields = ['nombre_municipio']
