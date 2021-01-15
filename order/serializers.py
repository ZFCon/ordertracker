from rest_framework import serializers

from .models import *


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = "__all__"
