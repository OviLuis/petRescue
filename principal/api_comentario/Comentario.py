from rest_framework import viewsets


from principal.models import Comentario
from principal.serializers import *


class ComentarioAPI(viewsets.ModelViewSet):
    """docstring for ComentarioAPI"""
    model = Comentario
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()

    def pre_save(self, obj):
        obj.usuario = self.request.user
