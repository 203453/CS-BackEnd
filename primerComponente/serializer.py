import email
from django.db import models
from rest_framework import routers, serializers, viewsets

# Importacion de modelos
from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ('__all__')
