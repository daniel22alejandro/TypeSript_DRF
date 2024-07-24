"""
URL configuration for coffco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.alquiler_laboratorio.api.router import router_alquiler
from apps.datos.api.router import router_datos
from apps.detalle.api.router import router_detalle
from apps.documentos.api.router import router_documentos
from apps.finca.api.router import router_finca
from apps.muestra.api.router import router_muestra
from apps.municipio.api.router import router_municipio
from apps.servicios.api.router import router_servicios
from apps.tipo_formato.api.router import router_tipo_formato
from apps.versiones.api.router import router_versiones



from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Coffco API",
      default_version='v1',
      description="A mucho honor este es el api de mi proyecto con django-restframework",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alquiler_laboratorio', include(router_alquiler.urls)),
    path('api/datos', include(router_datos.urls)),
    path('api/detalle', include(router_detalle.urls)),
    path('api/documentos', include(router_documentos.urls)),
    path('api/finca', include(router_finca.urls)),
    path('api/muestra', include(router_muestra.urls)),
    path('api/municipio', include(router_municipio.urls)),
    path('api/servicios', include(router_servicios.urls)),
    path('api/tipo_formato', include(router_tipo_formato.urls)),
    path('api/versiones', include(router_versiones.urls)),







    
    path('api/', include('apps.users.api.router')), #este para arreglos (listas), el otro es para funciones 




    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
