from rest_framework.routers import DefaultRouter
from apps.datos.api.views import datos_ModelViewSet

router_datos = DefaultRouter()
router_datos.register(prefix='mi_recurso', basename='mi_recurso', viewset=datos_ModelViewSet)
