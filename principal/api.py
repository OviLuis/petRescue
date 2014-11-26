from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import *
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
        """usuario = request.user
        try:
            perdido = Perdidos()
            perdido.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)"""
        #monto = request.DATA.get('monto')


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
