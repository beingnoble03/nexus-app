"""
ASGI config for nexus project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexus.settings')

django_application = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from nexus_app import routing
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
    "http": django_application,
})