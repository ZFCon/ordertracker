from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import *
from .serializers import *


def index(request):
    return render(request, "order\index.html")


class OrderView(ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer


class DoerRequestView(ModelViewSet):
    queryset = DoerRequest.objects.all()
    serializer_class = DoerRequestSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.filter(order=self.kwargs['order_pk'])
