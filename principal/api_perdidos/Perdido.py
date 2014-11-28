from principal.models import Perdidos
from principal.serializers import *

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class PerdidoCRUD(viewsets.ModelViewSet):
    """Clase para crud"""
    model = Perdidos
    serializer_class = PerdidoSerializer
    queryset = Perdidos.objects.all()
    permission_classes = (IsAuthenticated,)

    def pre_save(self, obj):
        obj.usuario = self.request.user


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PerdidoAPI(APIView):
    """docstring for PerdidoPublicacionAPI"""

    def get(self, request, *args, **kwargs):
        perdidos = Perdidos.objects.all()
        serializado = PerdidoSerializer(perdidos, many=True)
        return Response(serializado.data, status=status.HTTP_200_OK)
