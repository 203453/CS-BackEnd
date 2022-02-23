# from django.shortcuts import render

from django.contrib.auth.models import User
from .serializer import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class UserAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer