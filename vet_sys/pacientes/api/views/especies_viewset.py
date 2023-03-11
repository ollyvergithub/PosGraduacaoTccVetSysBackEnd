from rest_framework import viewsets
from ..serializers.especie_serializer import EspecieSerializer
from ...models import Especie


class EspeciesViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer
