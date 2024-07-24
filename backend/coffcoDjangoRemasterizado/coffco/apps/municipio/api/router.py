from rest_framework.routers import DefaultRouter
from apps.municipio.api.views import municipio_ModelViewSet

router_municipio = DefaultRouter()
router_municipio.register(prefix='mi_recurso', basename='mi_recurso', viewset=municipio_ModelViewSet)
