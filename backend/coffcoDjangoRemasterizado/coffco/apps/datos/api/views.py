from rest_framework.viewsets import ModelViewSet
from apps.datos.models import Datos
from apps.datos.api.serializer import datos_Serializer

class datos_ModelViewSet(ModelViewSet):
    serializer_class = datos_Serializer
    queryset = Datos.objects.all()