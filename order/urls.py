from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from . import views


router = DefaultRouter()
router.register('order', views.OrderView, basename='order')

order_router = NestedDefaultRouter(router, 'order', lookup='order')
order_router.register('requests', views.DoerRequestView,
                      basename='order-requests')

urlpatterns = [
    path('order/', views.index),
    path('api/', include(router.urls)),
    path('api/', include(order_router.urls)),
]
