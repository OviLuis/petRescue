from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import *
from .forms import *
from .serializers import *


class PerdidoAPI(APIView):
    """
    retorna
    """
    def get(self, request, format=None):
        perdidos = Perdidos.objects.all()
        serializado = PerdidoSerializer(perdidos, many=True)
        return Response(serializado.data)

    """
    crea
    """
    def post(self, request, format=None):
        usuario = request.user
        #print request.DATA
        nombre = request.DATA.get('nombre')
        raza = request.DATA.get('raza')
        edad = request.DATA.get('edad')
        especie = request.DATA.get('especie')
        sexo = request.DATA.get('sexo')
        foto = request.DATA.get('foto')
        descripcion = request.DATA.get('descripcion')
        fecha = request.DATA.get('fechaDesaparicion')
        direccion = request.DATA.get('dirDesaparicion')
        try:
            Perdidos(usuario=usuario, nombre=nombre, raza=raza, edad=edad, especie=especie, sexo=sexo, foto=foto, descripcion=descripcion, fechaDesaparicion=fecha, dirDesaparicion=direccion).save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)


from django.contrib.auth import login, logout, authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class AuthView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):
        email = request.DATA.get('email', None)
        password = request.DATA.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            serializer = UsuarioSerializer(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)
