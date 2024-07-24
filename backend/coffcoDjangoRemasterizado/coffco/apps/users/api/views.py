#logica de la app para crear los metodos mi papacho 
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response

from apps.users.api.serializer import UserRegisterSerializer,UserSerializer, UserUpdateSerializer


from apps.users.models import User


from rest_framework.permissions import IsAuthenticated

#registrar usuarios
class RegisterAPIView(APIView):
    #override del metodo post
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): #si llega a haber un error no retorne mano
            serializer.save() #SI es valido entonces guardelo en el modelo 
            return Response(serializer.data, status=status.HTTP_201_CREATED) #restorna respuesta


        return Response(serializer.errros, status=status.HTTP_400_BAD_REQUEST) #si hay error en los datos retorne el error



#listar datos del usuario
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    #override del metodo get 
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    #override del metodo actualizar
    def put(self, request):
        user = User.objects.get(pk=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

