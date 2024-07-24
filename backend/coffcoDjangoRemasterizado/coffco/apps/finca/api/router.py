from rest_framework.routers import DefaultRouter
from apps.finca.api.views import finca_ModelViewSet

router_finca = DefaultRouter()
router_finca.register(prefix='mi_recurso', basename='mi_recurso', viewset=finca_ModelViewSet)
