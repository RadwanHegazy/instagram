import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from .middleware import TokenAuthMiddleware
from django.urls import path
from chat.ws.routing import ws_urlpatterns
from dj_notification.consumer import NotificationConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django_asgi_app = get_asgi_application()

urls = ws_urlpatterns + [
    path('ws/notification', NotificationConsumer.as_asgi())
]

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            TokenAuthMiddleware(URLRouter(urls))
        ),
        
    }
)