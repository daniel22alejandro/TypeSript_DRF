#logica de la app para crear los metodos mi papacho 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from apps.users.models import User
from rest_framework.response import Response
from apps.users.api.serializer import UserSerializer,UserUpdate,UserGetSerializer
from rest_framework import serializers


class UserRegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_data = {
                "message": "Usuario Registrado Exitosamente",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class UserView(APIView):
  
    def get(self, request):
        users = User.objects.all()
        serializer = UserGetSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request):
        user=User.objects.get(pk=request.user.id)
        serializer = UserUpdate(user,request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        

class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EnumRolView(APIView):
    enumRol = serializers.SerializerMethodField()
    def get(self,request):
        return Response(User.enumRol)
class EnumTipoIdView(APIView):
    enumTipo = serializers.SerializerMethodField()   
    def get(self,request):
        return Response(User.enumTipo)             
