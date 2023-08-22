"""
ASGI config for Core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
from channels.routing import (
     ProtocolTypeRouter,
     URLRouter
)
from channels.auth import AuthMiddlewareStack
import os
from ChatRoom.webscoket_router import websocket_urlpatterns

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')

application = ProtocolTypeRouter(
     {
          "http":get_asgi_application(),
          'websocket':AuthMiddlewareStack(
               URLRouter(
                    websocket_urlpatterns
               )
          )
     }
)
