from rest_framework import viewsets
#from rest_framework.response import Response


from principal.models import Usuario
from principal.serializers import UsuarioSerializer


class UsuarioAPI(viewsets.ModelViewSet):
    model = Usuario
    serializer_class = UsuarioSerializer

