from rest_framework import viewsets


from principal.models import Adopciones
from principal.serializers import *


class AdopcionAPI(viewsets.ModelViewSet):
    """docstring for ComentarioAPI"""
    model = Adopciones
    serializer_class = AdopcionSerializer
    queryset = Adopciones.objects.all()

    def pre_save(self, obj):
        obj.usuario = self.request.user
