from rest_framework.viewsets import ModelViewSet
from apps.tipo_formato.models import TipoFormato
from apps.tipo_formato.api.serializer import tipo_formato_Serializer

class tipo_formato_ModelViewSet(ModelViewSet):
    serializer_class = tipo_formato_Serializer
    queryset = TipoFormato.objects.all()