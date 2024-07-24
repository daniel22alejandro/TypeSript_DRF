from rest_framework.routers import DefaultRouter
from apps.servicios.api.views import servicios_ModelViewSet

router_servicios = DefaultRouter()
router_servicios.register(prefix='mi_recurso', basename='mi_recurso', viewset=servicios_ModelViewSet)
