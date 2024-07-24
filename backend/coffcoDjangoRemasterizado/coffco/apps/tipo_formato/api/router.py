from rest_framework.routers import DefaultRouter
from apps.tipo_formato.api.views import tipo_formato_ModelViewSet

router_tipo_formato = DefaultRouter()
router_tipo_formato.register(prefix='mi_recurso', basename='mi_recurso', viewset=tipo_formato_ModelViewSet)
