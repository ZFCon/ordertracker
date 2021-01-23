from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/order/', consumers.OrderConsumer.as_asgi()),
]
