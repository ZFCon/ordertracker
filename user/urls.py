from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from . import views


urlpatterns = [
    path("api/auth/", ObtainAuthToken.as_view()),
    path("api/user/", views.UserView.as_view()),
]
