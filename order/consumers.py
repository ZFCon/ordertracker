from django.db.models import signals
from django.dispatch import receiver
from channels.generic.websocket import JsonWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import json
import logging

from .models import *


class OrderConsumer(JsonWebsocketConsumer):
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

    def order_saved(self, event):
        id = event['id']
        created = event['created']
        content_type = 'created' if created else 'updated'

        # the content that will go for the front-end
        content = {
            "type": content_type,
            "id": id,
        }

        # Send message to WebSocket
        self.send_json(content=content)

    def order_deleted(self, event):
        id = event['id']

        # the content that will go for the front-end
        content = {
            "type": 'deleted',
            "id": id,
        }

        # Send message to WebSocket
        self.send_json(content=content)

    @staticmethod
    @receiver(signals.post_save, sender=Order)
    def order_observer_saved(sender, instance, created, **kwargs):
        layer = get_channel_layer()

        async_to_sync(layer.group_send)('orders', {
            'type': 'order.saved',
            'created': created,
            'id': instance.id,
        })

    @staticmethod
    @receiver(signals.post_delete, sender=Order)
    def order_observer_deleted(sender, instance, **kwargs):
        layer = get_channel_layer()

        async_to_sync(layer.group_send)('orders', {
            'type': 'order.deleted',
            'id': instance.id,
        })
