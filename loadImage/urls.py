from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import views

# Importacion de vistas
from loadImage.views import SegundaTablaList
from loadImage.views import SegundaTablaDetail

urlpatterns = [
    re_path(r'^imagen/$', SegundaTablaList.as_view()),
    re_path(r'^imagen/(?P<pk>\d+)$', SegundaTablaDetail.as_view()),
]