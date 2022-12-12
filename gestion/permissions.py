from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from django.contrib.auth.models import AnonymousUser

class SoloAdmin(BasePermission):
    message = 'Tu no tienes los permisos necesarios'

    def has_permission(self,request:Request,view):

        print(SAFE_METHODS)
        
        if request.method in SAFE_METHODS:
            return True

        if isinstance(request.user,AnonymousUser):
            return False

        print(request.user)
        print(view)
        
        if request.user.tipoUsuario == 'ADMIN':
            return True
        else:
            return False
    