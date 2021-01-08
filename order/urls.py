from django.urls import path

from . import views


urlpatterns = [
    path('order/', views.index),
    path('api/orders/', views.OrderView.as_view()),
]
