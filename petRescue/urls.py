from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'petRescue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('principal.urls')),
    url(r'^', include('web.urls', namespace='web')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.conf import settings
from django.contrib.staticfiles import views

"""
if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]
"""