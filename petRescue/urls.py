from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'petRescue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'principal.views.inicio', ),
    url(r'^perdidos/$', 'principal.views.perdidos', name='perdidos'),
    url(r'^repotarPerdido/$', 'principal.views.repotarPerdido', name='repotarPerdido'),
    url(r'^encontrados/$', 'principal.views.encontrados', name='encontrados'),
    url(r'^adopciones/$', 'principal.views.adopcion', name='adopciones'),
    url(r'^registro/$', 'principal.views.registro', name='registro'),




    url(r'^admin/', include(admin.site.urls)),
)
