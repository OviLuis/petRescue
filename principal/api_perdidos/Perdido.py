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

    """def create(self, request):
        print "create"
        print request.user
        serializer = PerdidoSerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            serializer.usuario = request.user
            #self.pre_save(serializer)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
    def pre_save(self, obj):
        print "pre save"
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
