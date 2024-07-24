from rest_framework.viewsets import ModelViewSet
from apps.documentos.models import Documentos
from apps.documentos.api.serializer import documentos_Serializer

class documentos_ModelViewSet(ModelViewSet):
    serializer_class = documentos_Serializer
    queryset = Documentos.objects.all()