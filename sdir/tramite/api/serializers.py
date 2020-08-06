from rest_framework import serializers
from ..models import Tramite, Cut

class TramiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tramite
        fields = ('paso','accion','fecha')
        read_only_fields = ('paso',)


class CutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cut
        fields = ('cut','ruc','codtramite')
        read_only_fields = ('cut',)







