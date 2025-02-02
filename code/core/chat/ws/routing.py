from .consumers import ChatConsumer
from django.urls import path

ws_urlpatterns = [
    path('ws/chat/<uuid:chat_id>/', ChatConsumer.as_asgi()),
]