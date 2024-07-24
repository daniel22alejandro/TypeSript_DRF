from rest_framework import serializers
from apps.versiones.models import Versiones
from apps.tipo_formato.models import TipoFormato
from apps.users.models import User
from apps.documentos.models import Documentos

class versiones_Serializer(serializers.ModelSerializer):
    fk_id_tipo_formato = serializers.PrimaryKeyRelatedField(queryset=TipoFormato.objects.all())
    fk_id_usuarios = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    fk_documentos = serializers.PrimaryKeyRelatedField(queryset=Documentos.objects.all())
    class Meta:
        model = Versiones
        fields = ['version', 'editable', 'fk_id_tipo_formato', 'fk_id_usuarios', 'formato_vacio', 'fk_documentos']
