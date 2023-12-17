# chat/routing.py
from django.urls import path

from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path(r"ws/chatroom", ChatConsumer.as_asgi()),
]
