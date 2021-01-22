from rest_framework import serializers

from .models import *
from .serializer_defaults import OrderUrlDefault
from .validators import HasDoderValidator
from user.serializers import UserSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


class DoerRequestSerializer(serializers.ModelSerializer):
    doer_details = UserSerializer(source='doer', read_only=True)
    doer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    order = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), default=OrderUrlDefault())

    class Meta:
        model = DoerRequest
        fields = '__all__'
        validators = [
            HasDoderValidator('order'),
        ]


class OrderSerializer(serializers.ModelSerializer):
    owner_details = serializers.StringRelatedField(
        source='owner', read_only=True)
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    doer_details = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    doer = serializers.StringRelatedField(read_only=True)

    requests = DoerRequestSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
