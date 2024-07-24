from apps.users.api.views import RegisterAPIView
from apps.users.api.views import UserView
from django.urls import path 

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view()), #registrar usuarios
    path('auth/me/', UserView.as_view()), #listar usuarios

    
    path('auth/login/', TokenObtainPairView.as_view()), #obtener el token
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/', TokenObtainPairView.as_view()), #verificar el token
    
]
