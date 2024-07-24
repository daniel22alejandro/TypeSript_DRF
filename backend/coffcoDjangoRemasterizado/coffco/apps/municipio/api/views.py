from rest_framework.viewsets import ModelViewSet
from apps.municipio.models import Municipio
from apps.municipio.api.serializer import municipio_Serializer

class municipio_ModelViewSet(ModelViewSet):
    serializer_class = municipio_Serializer
    queryset = Municipio.objects.all()