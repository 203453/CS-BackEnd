from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import views
from rest_framework_simplejwt.views import TokenRefreshView

from Login.views import LoginAuth, MyObtainTokenPairView

urlpatterns = [
    re_path(r'^v1/login', LoginAuth.as_view()),
    re_path(r'^v2/login', MyObtainTokenPairView.as_view()),
    re_path(r'^v2/refresh', TokenRefreshView.as_view()),
]