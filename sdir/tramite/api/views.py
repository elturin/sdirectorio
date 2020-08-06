from rest_framework.generics import ListAPIView, CreateAPIView
from django.db.models import Max, Case, When
from .serializers import TramiteSerializer, CutSerializer
from ..models import Tramite, Cut
from entidades.models import Entidad
import string
import random

class TramitesApiView(ListAPIView):
    serializer_class = TramiteSerializer
    queryset = Tramite.objects.all()

    def get_queryset(self):
        cut = self.kwargs.get('cut')
        if cut is not None:
            return Tramite.objects.filter(cut=cut)

class CutsApiView(CreateAPIView):
    serializer_class = CutSerializer
    queryset = Cut.objects.all()



    def perform_create(self, serializer):

        ruc = self.request.data['ruc']
        nomb = Entidad.objects.filter(ruc=ruc)
        print(nomb)
        if not nomb:
            nombx = 'NINGUN'
        else:
            nombx = nomb[0]

        cutmax = Cut.objects.filter(ruc=ruc).aggregate(Max('numero'))
        print(cutmax)

        if cutmax['numero__max'] is None:
            cutmax1 = 1
        else:
            cutmax1 = cutmax['numero__max']+1

        cutx=str(nombx)+str(cutmax1).zfill(5)+str(random.choice(string.ascii_letters).upper())

        serializer.save(cut=cutx, numero = cutmax1)



