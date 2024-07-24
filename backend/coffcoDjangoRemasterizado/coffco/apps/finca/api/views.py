from rest_framework.viewsets import ModelViewSet
from apps.finca.models import Finca
from apps.finca.api.serializer import finca_Serializer

class finca_ModelViewSet(ModelViewSet):
    serializer_class = finca_Serializer
    queryset = Finca.objects.all()