from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

	url(r'^$','web.views.inicio', name='inicio' ),
	url(r'^perdidos/$', 'web.views.perdidos', name='perdidos'),
    url(r'^reportarPerdido/$', 'web.views.reportarPerdido', name='reportarPerdido'),
    url(r'^encontrados/$', 'web.views.encontrados', name='encontrados'),
    url(r'^reportarEncontrado/$', 'web.views.reportarEncontrado', name='reportarEncontrado'),
    url(r'^adopciones/$', 'web.views.adopcion', name='adopciones'),
    url(r'^reportarAdopcion/$', 'web.views.reportarAdopcion', name='reportarAdopcion'),
    url(r'^registro/$', 'web.views.registro', name='registro'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root':settings.MEDIA_ROOT,}
       ),

 )