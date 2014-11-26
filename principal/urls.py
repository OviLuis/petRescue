from django.conf.urls import patterns, url
from .api import *

urlpatterns = patterns(
    '',
    url(r'^perdido', PerdidoAPI.as_view()),
    #url(r'^encontrado', EncontradoAPI.as_view()),
    #url(r'^adopcion', AdopcionAPI.as_view()),
    url(r'^auth', AuthView.as_view()),)
