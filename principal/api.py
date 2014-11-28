
from .serializers import *


def function(offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    perdidos = Perdidos.objects.filter(dt)
    return perdidos
