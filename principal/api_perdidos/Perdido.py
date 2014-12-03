from principal.models import Perdidos
from principal.serializers import *

from django.core.paginator import Paginator, PageNotAnInteger

from rest_framework import viewsets


class PerdidoCRUD(viewsets.ModelViewSet):
    """Clase para crud"""
    model = Perdidos
    serializer_class = PerdidoSerializer

    def get(self, pk):
        pass

    def get_queryset(self):
        return Perdidos.objects.filter(usuario=self.request.user)

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


"""    def get(self, request):
        perdidos = Perdidos.objects.all()
        serializado = PerdidoSerializer(perdidos, many=True)
        paginator = Paginator(perdidos, 50)
        page = request.QUERY_PARAMS.get('page')
        try:
            perdidos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            perdidos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999),
            # deliver last page of results.
            perdidos = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = PaginatePerdidos(perdidos, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
"""