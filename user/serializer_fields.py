from rest_framework import serializers

from .serializers import UserSerializer

from django.contrib.auth import get_user_model
User = get_user_model()
