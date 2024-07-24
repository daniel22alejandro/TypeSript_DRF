from rest_framework.routers import DefaultRouter
from apps.versiones.api.views import versiones_ModelViewSet

router_versiones = DefaultRouter()
router_versiones.register(prefix='mi_recurso', basename='mi_recurso', viewset=versiones_ModelViewSet)
