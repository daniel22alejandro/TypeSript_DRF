from rest_framework.routers import DefaultRouter
from apps.muestra.api.views import muestra_ModelViewSet

router_muestra = DefaultRouter()
router_muestra.register(prefix='mi_recurso', basename='mi_recurso', viewset=muestra_ModelViewSet)
