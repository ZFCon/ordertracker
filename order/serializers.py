from rest_framework import serializers

from .models import *
from user.serializers import UserSerializer


class DoerRequestSerializer(serializers.ModelSerializer):
    doer = serializers.StringRelatedField()

    class Meta:
        model = DoerRequest
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    owner = UserSerializer(default=serializers.CurrentUserDefault())
    doer = serializers.StringRelatedField(read_only=True)
    requests = DoerRequestSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
