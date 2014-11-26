from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'petRescue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'web.views.inicio', ),
    url(r'^perdidos/$', 'web.views.perdidos', name='perdidos'),
    url(r'^repotarPerdido/$', 'web.views.repotarPerdido', name='repotarPerdido'),
    url(r'^encontrados/$', 'web.views.encontrados', name='encontrados'),
    url(r'^adopciones/$', 'web.views.adopcion', name='adopciones'),
    url(r'^registro/$', 'web.views.registro', name='registro'),




    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('principal.urls')),
)
