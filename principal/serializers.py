from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    """docstring for UsuarioSerializer"""
    class Meta:
        """docstring for Meta"""
        model = Usuario
        fields = ('id', 'email', 'nombre', 'direccion', 'telefono', 'password')
        read_only_fields = ('id', )
        write_only_fields = ('password', )

    def restore_object(self, attrs, instance=None):
        print "RESTOURE "+attrs['password']
        user = super(UsuarioSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class PerdidoSerializer(serializers.ModelSerializer):
    """docstring for ClassName"""
    class Meta:
        """docstring for Meta"""
        model = Perdidos


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


class ComentarioSerializer(serializers.ModelSerializer):
    """docstring for ComentarioSerializer"""
    class Meta:
        """docstring for Meta"""
        model = Comentario
