from rest_framework import serializers
from rest_framework.pagination import *
from rest_framework import pagination

from .models import * 



class PerdidoSerializer(serializers.ModelSerializer):
    """docstring for ClassName"""
    class Meta:
        """docstring for Meta"""
        model = Perdidos


class PaginatePerdidos(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = PerdidoSerializer
        


class EncontradoSerializer(serializers.ModelSerializer):
    """docstring for ClassName"""
    class Meta:
        """docstring for Meta"""
        model = Encontrados
        #fields = ('nombre', 'raza', 'edad', 'especie', 'sexo', 'foto', 'descripcion', 'fechaEncuentro', 'dirEncuentro')


class AdopcionSerializer(serializers.ModelSerializer):
    """docstring for ClassName"""
    class Meta:
        """docstring for Meta"""
        model = Adopciones
        #fields = ('nombre', 'raza', 'edad', 'especie', 'sexo', 'foto', 'descripcion', 'direccion', )


class UsuarioSerializer(serializers.ModelSerializer):
    """docstring for UsuarioSerializer"""

    class Meta:
        """docstring for Meta"""
        model = Usuario
        fields = ('id', 'email', 'nombre', 'direccion', 'telefono', 'password')#, 'comentarios')
        read_only_fields = ('id', )
        write_only_fields = ('password', )

    def restore_object(self, attrs, instance=None):
        print "RESTOURE "+attrs['password']
        user = super(UsuarioSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user

#class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
class ComentarioSerializer(serializers.ModelSerializer):
    """docstring for ComentarioSerializer"""
    #usuario = serializers.HyperlinkedIdentityField(view_name='usuario')
    usuario = UsuarioSerializer(many=False)


    class Meta:
        """docstring for Meta"""
        model = Comentario
        fields = ('id', 'texto', 'mascota', 'fechaPublicacion', 'usuario')
        usuario = serializers.Field(source='usuario')




