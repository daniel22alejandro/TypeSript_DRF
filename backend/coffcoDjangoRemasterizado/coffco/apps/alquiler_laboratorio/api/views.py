from rest_framework.viewsets import ModelViewSet
from apps.alquiler_laboratorio.models import AlquilerLaboratorio
from apps.alquiler_laboratorio.api.serializer import alquiler_Serializer

class alquiler_ModelViewSet(ModelViewSet):
    serializer_class = alquiler_Serializer
    queryset = AlquilerLaboratorio.objects.all()