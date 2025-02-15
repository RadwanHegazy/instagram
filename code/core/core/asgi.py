import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Initialize Django ASGI application early to ensure the AppRegistry is populated
django_asgi_app = get_asgi_application()

# Now it's safe to import other Django modules
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat.ws.routing import ws_urlpatterns
from dj_notification.consumer import NotificationConsumer
from django.urls import path
from .middleware import TokenAuthMiddleware

# Define WebSocket URL patterns
urls = ws_urlpatterns + [
    path('ws/notification', NotificationConsumer.as_asgi())
]

# Define the ASGI application
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            TokenAuthMiddleware(URLRouter(urls))
        ),
    }
)