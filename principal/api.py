
from .serializers import *


def function(offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    perdidos = Perdidos.objects.filter(dt)
    return perdidos




#from rest_framework import viewsets
#from rest_framework.permissions import AllowAny



    """
    retorna
    
    def get(self, request, format=None):
        perdidos = Perdidos.objects.get(pk=1)
        serializado = PerdidoSerializer(perdidos, many=True)
        return Response(serializado.data)

    """