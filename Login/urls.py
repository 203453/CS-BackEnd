from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import views


from Login.views import LoginAuth

urlpatterns = [
    re_path(r'^', LoginAuth.as_view()),
]