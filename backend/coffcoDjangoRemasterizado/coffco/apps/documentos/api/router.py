from rest_framework.routers import DefaultRouter
from apps.documentos.api.views import documentos_ModelViewSet

router_documentos = DefaultRouter()
router_documentos.register(prefix='mi_recurso', basename='mi_recurso', viewset=documentos_ModelViewSet)
