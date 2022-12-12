from .models import UsuarioModel,CineModel,SalaModel,AsientoModel
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):

    def save(self):

        nuevoUsuario = UsuarioModel(**self.validated_data)

        nuevoUsuario.set_password(self.validated_data.get('password'))

        nuevoUsuario.save()

        return nuevoUsuario
    class Meta:
        fields = '__all__'
        model = UsuarioModel
        extra_kwargs={
            'password':{
                'write_only':True
            },
            'id':{
                'read_only':True
            }
        }

class CineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CineModel
        extra_kwargs={
            'id':{
                'read_only':True
            }
        }
        
class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SalaModel
        extra_kwargs={
            'id':{
                'read_only':True
            }
        }

class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AsientoModel
        extra_kwargs={
            'id':{
                'read_only':True
            }
        }