import email
from django.db import models
from rest_framework import routers, serializers, viewsets
# Importacion de modelos
from loadImage.models import SegundaTabla

class SegundaTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegundaTabla
        fields = ('id', 'name_img', 'url_img', 'format_img')