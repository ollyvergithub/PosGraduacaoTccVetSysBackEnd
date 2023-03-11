from rest_framework import viewsets
from ..serializers.porte_serializer import PorteSerializer
from ...models import Porte


class PortesViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = Porte.objects.all()
    serializer_class = PorteSerializer
