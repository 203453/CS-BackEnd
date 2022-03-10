from dataclasses import field
from rest_framework import serializers

from Profile.models import TercerTabla

class TercerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TercerTabla
        fields = ('__all__')