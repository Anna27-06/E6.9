from django.urls import re_path

from . import action
# Создание соединения для каждого отдельного класса
websocket_urlpatterns = [
    re_path(r'ws/Back/(?P<room_name>\w+)/$', action.ChatConsumer.as_asgi()),
]