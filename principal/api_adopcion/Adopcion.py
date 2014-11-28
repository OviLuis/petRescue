from rest_framework import viewsets


from principal.models import Adopciones
from principal.serializers import *


class AdopcionCRUD(viewsets.ModelViewSet):
    """docstring for ComentarioAPI"""
    model = Adopciones
    serializer_class = AdopcionSerializer
    queryset = Adopciones.objects.all()

    def pre_save(self, obj):
        obj.usuario = self.request.user

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AdopcionAPI(APIView):
    """docstring for PerdidoPublicacionAPI"""

    def get(self, request, *args, **kwargs):
        adoptados = Adopciones.objects.all()
        serializado = AdopcionesSerializer(adoptados, many=True)
        return Response(serializado.data, status=status.HTTP_200_OK)
