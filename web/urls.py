from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('',

  url(r'^$', 'web.views.inicio', name='inicio'),
  url(r'^perdidos/$', 'web.views.perdidos', name='perdidos'),
  url(r'^reportarPerdido/$', 'web.views.reportarPerdido', name='reportarPerdido'),
  url(r'^encontrados/$', 'web.views.encontrados', name='encontrados'),
  url(r'^reportarEncontrado/$', 'web.views.reportarEncontrado', name='reportarEncontrado'),
  url(r'^adopciones/$', 'web.views.adopcion', name='adopciones'),
  url(r'^reportarAdopcion/$', 'web.views.reportarAdopcion', name='reportarAdopcion'),
  url(r'^perdidos/(?P<mascota_id>\d+)/$', 'web.views.detail', name='detail'),
  url(r'^encontrados/(?P<mascota_id>\d+)/$', 'web.views.detail', name='encontrados'),
  url(r'^adopciones/(?P<mascota_id>\d+)/$', 'web.views.detail', name='detail'),
  url(r'^miCuenta/$', 'web.views.miCuenta', name='miCuenta'),
  url(r'^ayuda/$', 'web.views.ayuda', name='ayuda'),
  url(r'^h/$', 'web.views.h',),
  url(r'^u/$', 'web.views.u',),

  url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root':settings.MEDIA_ROOT,}
  ),


)


handler404 = 'web.views.error404'


