from rest_framework.viewsets import ModelViewSet
from apps.detalle.models import Detalle
from apps.detalle.api.serializer import detalle_Serializer

class detalle_ModelViewSet(ModelViewSet):
    serializer_class = detalle_Serializer
    queryset = Detalle.objects.all()