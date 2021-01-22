from django.db.models.query import QuerySet
from rest_framework import serializers

from .models import *
from .serializer_defaults import OrderUrlDefault
from .validators import HasDoderValidator
from user.serializers import UserSerializer


class DoerRequestSerializer(serializers.ModelSerializer):
    doer = UserSerializer(default=serializers.CurrentUserDefault())
    order = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), default=OrderUrlDefault())

    class Meta:
        model = DoerRequest
        fields = '__all__'
        validators = [
            HasDoderValidator('order'),
        ]


class OrderSerializer(serializers.ModelSerializer):
    owner = UserSerializer(default=serializers.CurrentUserDefault())
    doer = serializers.StringRelatedField(read_only=True)
    requests = DoerRequestSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
