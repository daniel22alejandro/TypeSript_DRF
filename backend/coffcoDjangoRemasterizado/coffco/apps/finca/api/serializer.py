from rest_framework import serializers
from apps.finca.models import Finca
from apps.users.models import User
from apps.municipio.models import Municipio

class finca_Serializer(serializers.ModelSerializer):
    fk_id_usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    fk_id_municipio = serializers.PrimaryKeyRelatedField(queryset=Municipio.objects.all())
    class Meta:
        model = Finca
        fields = ['nombre_finca', 'fk_id_municipio', 'fk_id_usuario']
