"""
WSGI config for petRescue project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "petRescue.settings")
from django.core.wsgi import get_wsgi_application

DEBUG = False

if DEBUG:
    application = get_wsgi_application()
else:
    from dj_static import Cling
    application = Cling(get_wsgi_application())
