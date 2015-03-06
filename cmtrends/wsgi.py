"""
WSGI config for cmtrends project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmtrends.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

proxy_addres = "127.0.0.1:3128"

os.environ["http_proxy"] = "http://"+proxy_addres
os.environ["https_proxy"] = "https://"+proxy_addres