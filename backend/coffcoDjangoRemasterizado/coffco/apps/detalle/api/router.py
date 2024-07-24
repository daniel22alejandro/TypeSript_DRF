from rest_framework.routers import DefaultRouter
from apps.detalle.api.views import detalle_ModelViewSet

router_detalle = DefaultRouter()
router_detalle.register(prefix='mi_recurso', basename='mi_recurso', viewset=detalle_ModelViewSet)
