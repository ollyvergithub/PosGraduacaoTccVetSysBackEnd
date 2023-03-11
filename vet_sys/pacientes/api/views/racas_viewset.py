from rest_framework import viewsets
from ..serializers.raca_serializer import RacaSerializer
from ...models import Raca


class RacasViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer
