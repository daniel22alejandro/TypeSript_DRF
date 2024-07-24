from rest_framework.viewsets import ModelViewSet
from apps.servicios.models import Servicios
from apps.servicios.api.serializer import servicios_Serializer

class servicios_ModelViewSet(ModelViewSet):
    serializer_class = servicios_Serializer
    queryset = Servicios.objects.all()