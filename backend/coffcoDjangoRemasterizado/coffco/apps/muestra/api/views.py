from rest_framework.viewsets import ModelViewSet
from apps.muestra.models import Muestra
from apps.muestra.api.serializer import muestra_Serializer

class muestra_ModelViewSet(ModelViewSet):
    serializer_class = muestra_Serializer
    queryset = Muestra.objects.all()