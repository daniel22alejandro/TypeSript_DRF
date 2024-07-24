from rest_framework.viewsets import ModelViewSet
from apps.versiones.models import Versiones
from apps.versiones.api.serializer import versiones_Serializer

class versiones_ModelViewSet(ModelViewSet):
    serializer_class = versiones_Serializer
    queryset = Versiones.objects.all()