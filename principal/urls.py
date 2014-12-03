from django.conf.urls import patterns, url, include
from .api import *

from .api_autenticacion import Autenticacion


from rest_framework import routers


from .api_usuario import Usuario
usuario = routers.DefaultRouter()
usuario.register(r'usuario/edit', Usuario.UsuarioAPI)


from .api_perdidos import Perdido
perdido = routers.DefaultRouter()
perdido.register(r'perdido/edit', Perdido.PerdidoCRUD)


from .api_encontrado import Encontrado
encontrado = routers.DefaultRouter()
encontrado.register(r'encontrado/edit', Encontrado.EncontradoCRUD)


from .api_adopcion import Adopcion
adopcion = routers.DefaultRouter()
adopcion.register(r'adopcion', Adopcion.AdopcionCRUD)


from .api_comentario import Comentario
comentario = routers.DefaultRouter()
comentario.register(r'comentario/edit', Comentario.ComentarioCRUD)


#PAra traer los comentarios
#perdido_comentarios = routers.DefaultRouter()
#perdido_comentarios.register('comentario', Comentario.ComentarioAPI)


import api

urlpatterns = patterns(
    '',
    #urls para CRUD
    url(r'^api/', include(usuario.urls)),
    url(r'^api/', include(perdido.urls)),
    url(r'^api/', include(encontrado.urls)),
    url(r'^api/', include(adopcion.urls)),
    url(r'^api/', include(comentario.urls)),

    #urls publicas
    url(r'^api/perdido/$', Perdido.PerdidoAPI.as_view()),
    url(r'^api/encontrado/', Encontrado.EncontradoAPI.as_view()),

    url(r'^api/comentario/(?P<id_mascota>\d+)', Comentario.ComentarioAPI.as_view()),


#
#
    url(r'^api/auth', Autenticacion.AuthView.as_view()),)

