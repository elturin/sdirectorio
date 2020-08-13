from rest_framework import serializers
from ..models import Tramite, Cut, TramiteUnico
from entidades.models import Entidad

class TramiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tramite
        fields = ('paso','accion','fecha')
        read_only_fields = ('paso',)

class TramiteUnicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TramiteUnico
        fields = ('codigo','tramite')


class EntidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entidad
        fields = ('ruc','nombre')
        #read_only_fields = ('paso',)

class CutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cut
        fields = ('cut','ruc','codtramite')
        read_only_fields = ('cut',)







