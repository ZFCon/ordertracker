from django.db.models import signals
from django.dispatch import receiver
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import json
import logging

from .models import *


class TestConsumer(WebsocketConsumer):
    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            'test',
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            'test',
            self.channel_name
        )

    def receive(self, text_data):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            'test',
            {
                'type': 'data',
                'data': text_data
            }
        )

    # Receive message from room group
    def data(self, event):
        data = event['data']

        # Send message to WebSocket
        self.send(text_data=data)

    @staticmethod
    @receiver(signals.post_save, sender=Order)
    def order_offer_observer(sender, instance, **kwargs):
        layer = get_channel_layer()
        async_to_sync(layer.group_send)('test', {
            'type': 'data',
            'data': "something updated."
        })
