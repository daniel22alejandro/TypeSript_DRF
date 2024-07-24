# from rest_framework.permissions import BasePermission

# class IsAdminOrReadOnly(BasePermission):
 
#     def has_permission(self, request, view):
#         # Permitir los métodos seguros (GET, HEAD, OPTIONS) a todos los usuarios.
#         if request.method in ['GET', 'POST', 'DELETE']:
#             return True
#         # Permitir la actualización solo si el usuario es un administrador.
#         elif request.method == 'PUT' or request.method == 'PATCH':
#             return request.user and request.user.is_staff
#         return False

# class UpdateCart(BasePermission):
 
#     def has_permission(self, request, view):
#         # Permitir la actualización solo si el usuario es un administrador.
#         if request.method == 'PUT':
#             return request.user and request.user.is_staff
#         return False
