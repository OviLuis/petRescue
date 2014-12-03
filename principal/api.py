
from .serializers import *
from .models import Perdidos

from rest_framework.response import Response
from rest_framework import status




def publicaciones_recientes(offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    perdidos = Perdidos.objects.filter(dt)
    return perdidos
