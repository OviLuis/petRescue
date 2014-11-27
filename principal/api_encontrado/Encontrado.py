from rest_framework import viewsets


from principal.models import Encontrados
from principal.serializers import *


class EncontradoAPI(viewsets.ModelViewSet):
    """docstring for ComentarioAPI"""
    model = Encontrados
    serializer_class = EncontradoSerializer
    queryset = Encontrados.objects.all()

    #def list(self, request):
    #    return Response(EncontradoSerializer(Encontrados.objects.filter(usuario=request.user), many=True).data)

    def pre_save(self, obj):
        obj.usuario = self.request.user
