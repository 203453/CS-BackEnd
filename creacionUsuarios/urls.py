from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import views
from rest_framework_simplejwt.views import TokenRefreshView

from creacionUsuarios.views import UserAPI

urlpatterns = [
    re_path(r'^createUser/$', UserAPI.as_view()),
]