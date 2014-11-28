from rest_framework import viewsets


from principal.models import Encontrados
from principal.serializers import *


class EncontradoCRUD(viewsets.ModelViewSet):
    """docstring for ComentarioAPI"""
    model = Encontrados
    serializer_class = EncontradoSerializer
    queryset = Encontrados.objects.all()

    #def list(self, request):
    #    return Response(EncontradoSerializer(Encontrados.objects.filter(usuario=request.user), many=True).data)

    def pre_save(self, obj):
        obj.usuario = self.request.user


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EncontradoAPI(APIView):
    """docstring for PerdidoPublicacionAPI"""

    def get(self, request, *args, **kwargs):
        encontrados = Encontrados.objects.all()
        serializado = EncontradoSerializer(encontrados, many=True)
        return Response(serializado.data, status=status.HTTP_200_OK)
