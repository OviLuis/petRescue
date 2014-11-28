from django.conf.urls import patterns, url, include
from .api import *

from .api_autenticacion import Autenticacion


from rest_framework import routers


from .api_usuario import Usuario
usuario = routers.DefaultRouter()
usuario.register(r'usuario', Usuario.UsuarioAPI)


from .api_perdidos import Perdido
perdido = routers.DefaultRouter()
perdido.register(r'perdido', Perdido.PerdidoCRUD)


from .api_encontrado import Encontrado
encontrado = routers.DefaultRouter()
encontrado.register(r'encontrado', Encontrado.EncontradoCRUD)


from .api_adopcion import Adopcion
adopcion = routers.DefaultRouter()
adopcion.register(r'adopcion', Adopcion.AdopcionCRUD)


from .api_comentario import Comentario
comentario = routers.DefaultRouter()
comentario.register(r'comentario', Comentario.ComentarioCRUD)


#PAra traer los comentarios
#perdido_comentarios = routers.DefaultRouter()
#perdido_comentarios.register('comentario', Comentario.ComentarioAPI)


urlpatterns = patterns(
    '',
    url(r'^api/', include(usuario.urls)),
    url(r'^api/', include(perdido.urls)),
    url(r'^api/', include(encontrado.urls)),
    url(r'^api/', include(adopcion.urls)),
    url(r'^api/', include(comentario.urls)),

    url(r'^api/p/', Perdido.PerdidoAPI.as_view()),
#
#
    url(r'^api/auth', Autenticacion.AuthView.as_view()),)
