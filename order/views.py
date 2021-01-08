from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import *
from .serializers import *


def index(request):
    return render(request, "order\index.html")


class OrderView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
