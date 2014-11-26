from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

	url(r'^$','web.views.inicio', name='inicio' ),
	url(r'^perdidos/$', 'web.views.perdidos', name='perdidos'),
    url(r'^repotarPerdido/$', 'web.views.repotarPerdido', name='repotarPerdido'),
    url(r'^encontrados/$', 'web.views.encontrados', name='encontrados'),
    url(r'^adopciones/$', 'web.views.adopcion', name='adopciones'),
    url(r'^registro/$', 'web.views.registro', name='registro'),

 )