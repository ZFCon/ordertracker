from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import *
from .serializers import *


def index(request):
    return render(request, "order\index.html")


class OrderView(ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
