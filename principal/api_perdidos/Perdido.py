from rest_framework import viewsets


from principal.models import Perdidos
from principal.serializers import *


class PerdidoAPI(viewsets.ModelViewSet):
    """view that serves posts"""
    model = Perdidos
    serializer_class = PerdidoSerializer
    queryset = Perdidos.objects.all()
    #permission_classes = (permissions.IsOwner,)

    def pre_save(self, obj):
        obj.usuario = self.request.user



#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
