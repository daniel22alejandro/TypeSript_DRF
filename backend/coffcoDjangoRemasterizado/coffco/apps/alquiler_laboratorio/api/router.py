from rest_framework.routers import DefaultRouter
from apps.alquiler_laboratorio.api.views import alquiler_ModelViewSet

router_alquiler = DefaultRouter()
router_alquiler.register(prefix='mi_recurso', basename='mi_recurso', viewset=alquiler_ModelViewSet)
