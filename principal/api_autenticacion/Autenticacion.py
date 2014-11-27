from rest_framework.views import APIView

from django.contrib.auth import login, logout, authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


from principal.serializers import UsuarioSerializer

from rest_framework.response import Response
from rest_framework import status


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

"""{
    "email":"aslheyramirez@gmail.com",
    "password":"rizotas"
    }"""
