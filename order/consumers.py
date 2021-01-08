from django.db.models import signals
from django.dispatch import receiver
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import json
import logging

from .models import *
from .serializers import *


class OrderConsumer(WebsocketConsumer):
    group_name = "orders"

    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # This consumer should not have a receive method
    # def receive(self, text_data):
    #     # Send message to room group
    #     async_to_sync(self.channel_layer.group_send)(
    #         'test',
    #         {
    #             'type': 'data',
    #             'data': text_data
    #         }
    #     )

    # Receive message from room group
    def data(self, event):
        data = event['data']

        # Send message to WebSocket
        self.send(text_data=data)

    @staticmethod
    @receiver(signals.post_save, sender=Order)
    def order_observer(sender, instance, **kwargs):
        layer = get_channel_layer()
        data = OrderSerializer(instance=instance).data
        data = json.dumps(data)
        async_to_sync(layer.group_send)('orders', {
            'type': 'data',
            'data': data,
        })
