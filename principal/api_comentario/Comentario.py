from rest_framework import viewsets
from rest_framework.response import Response



from principal.models import Comentario
from principal.serializers import *

from django.contrib.auth.decorators import login_required


class ComentarioCRUD(viewsets.ModelViewSet):
    """docstring for ComentarioAPI"""
    model = Comentario
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()

    def list(self, request):
        queryset = Comentario.objects.all()
        serializer = ComentarioSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comentario.objects.filter(mascota=pk)
        serializer = ComentarioSerializer(queryset, many=True)
        return Response(serializer.data)

    def pre_save(self, obj):
        obj.usuario = self.request.user


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ComentarioAPI(APIView):
    """docstring for ComentarioAPI"""

    def get(self, request, id_mascota,  *args, **kwargs):
        comentarios = Comentario.objects.filter(mascota=id_mascota)
        serializado = ComentarioSerializer(comentarios, many=True)
        return Response(serializado.data, status=status.HTTP_200_OK)


"""    @action(permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):

        #Likes a review. User authentication is required.

        # I want no params for this action and I want to show a different serializer class.

        review = self.get_object()
        try:
            review.like(request.user.userprofile)
            return Response({}, status=status.HTTP_200_OK)
        except ReviewLikeExistException, e:
            return Response({'message': e.message}, status=status.HTTP_400_BAD_REQUEST)

 def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
"""
