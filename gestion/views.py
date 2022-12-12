from rest_framework.generics import CreateAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import UsuarioModel,SalaModel,CineModel,AsientoModel
from .serializers import UsuarioSerializer,SalaSerializer,CineSerializer,AsientoSerializer
from .permissions import SoloAdmin

class RegistroUsuarioApiView(ListCreateAPIView):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [SoloAdmin]

    def post(self, request: Request):
        informacion = self.serializer_class(data=request.data)

        es_valida=informacion.is_valid()

        if not es_valida:
            return Response(data={
                'message':'Error al crear usuario',
                'content':informacion.errors
            },status=status.HTTP_400_BAD_REQUEST)
        
        else:
            nuevoUsuario = informacion.save()
            nuevoUsuarioSerializado = self.serializer_class(instance=nuevoUsuario)

            return Response(data={
                'message':'Usuario creado exitosamente, ya se puede logear',
                'content': nuevoUsuarioSerializado.data
            },status=status.HTTP_201_CREATED)
    

    def get(self,request:Request):
        usuarios = UsuarioModel.objects.filter(tipoUsuario="USER").all()
        usuarios_serializados = self.serializer_class(instance=usuarios, many = True)
        return Response(data={
            'message':'Los usuarios tipo USER son:',
            'content': usuarios_serializados.data
        })
    def get(self,request:Request):
        usuarios = UsuarioModel.objects.filter(tipoUsuario="ADMIN").all()
        usuarios_serializados = self.serializer_class(instance=usuarios, many = True)
        return Response(data={
            'message':'Los usuarios tipo ADMIN son:',
            'content': usuarios_serializados.data
        })
    def get(self,request:Request):
        usuarios = self.get_queryset()
        usuarios_serializados = self.serializer_class(instance=usuarios, many = True)
        return Response(data={
            'message':'Los usuarios son:',
            'content': usuarios_serializados.data
        })

class RegistroCineApiView(ListCreateAPIView):
    queryset = CineModel.objects.all()
    serializer_class = CineSerializer

    def post(self,request:Request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        nuevoCine=data.save()
        return Response(data={
            'message':'Cine creado exitosamente',
            'content': self.serializer_class(instance=nuevoCine).data
        })
    def get(self,request:Request):
        cines = self.get_queryset()
        cines_serializados = self.serializer_class(instance=cines, many = True)
        return Response(data={
            'message':'Los cines son:',
            'content': cines_serializados.data
        })

class RegistroSalaApiView(CreateAPIView):
    queryset = SalaModel.objects.all()
    serializer_class = SalaSerializer

    def post(self,request:Request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        nuevoCine=data.save()
        return Response(data={
            'message':'Sala creada exitosamente',
            'content': self.serializer_class(instance=nuevoCine).data
        })
    def get(self,request:Request):
        salas = self.get_queryset()
        salas_serializados = self.serializer_class(instance=salas, many = True)
        return Response(data={
            'message':'Las salas son:',
            'content': salas_serializados.data
        })
        
class SalaUpdateApiView(UpdateAPIView):
    queryset = SalaModel.objects.all()
    serializer_class = SalaSerializer

class SalaDeleteApiView(DestroyAPIView):
    queryset = SalaModel.objects.all()
    serializer_class = SalaSerializer

class RegistroAsientoApiView(ListCreateAPIView):
    queryset = AsientoModel.objects.all()
    serializer_class = AsientoSerializer

    def post(self,request:Request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        nuevoCine=data.save()
        return Response(data={
            'message':'Asiento creado exitosamente',
            'content': self.serializer_class(instance=nuevoCine).data
        })

class AsientoToggleApiView(ListCreateAPIView):
    queryset = AsientoModel.objects.all()
    serializer_class = AsientoSerializer

    def put(self,request:Request):
        asientoEncontrado = AsientoModel.objects.filter(id=id).first()

        if asientoEncontrado is None:
            return Response(data={
                'message':'Asiento no encontrado',
            }, status = status.HTTP_404_NOT_FOUND)

        asientoEncontrado.disponibilidad=not asientoEncontrado.disponibilidad
        asientoEncontrado.save()

        return Response(data={
            'message':'Asiento actualizado exitosamente',
            'content': self.serializer_class(instance=asientoEncontrado).data
        },status=status.HTTP_201_CREATED)

class AsientoDisponibleApiView(ListCreateAPIView):

    queryset = AsientoModel.objects.all()
    serializer_class = AsientoSerializer

    def get(self,request:Request):
        asientos = AsientoModel.objects.filter(disponibilidad=True).all()
        asientos_serializados = self.serializer_class(instance=asientos,many=True)

        return Response(data={
            'message':'Los platos son:',
            'content': asientos_serializados.data
        })
    
class VistaProtegidaApiView(ListAPIView):
    queryset = SalaModel.objects.all()
    serializer_class = SalaSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes=[SoloAdmin]

    def get(self, request:Request):
        print('El auth es:' ,request.auth)
        print('El user es:' ,request.user)

        return Response(data={
            'message':'Hola',
            'usuario':
                {'id':request.user.id,
                'correo':request.user.correo}
        })
