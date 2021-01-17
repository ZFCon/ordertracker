from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('orders', views.OrderView, basename='orders')

urlpatterns = [
    path('order/', views.index),
    path('api/', include(router.urls)),
]
