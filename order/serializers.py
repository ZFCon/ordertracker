from rest_framework import serializers

from .models import *


class DoerRequestSerializer(serializers.ModelSerializer):
    doer = serializers.StringRelatedField()

    class Meta:
        model = DoerRequest
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    doer = serializers.StringRelatedField()
    requests = DoerRequestSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
