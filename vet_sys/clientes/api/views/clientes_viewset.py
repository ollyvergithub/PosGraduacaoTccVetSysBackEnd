from rest_framework import viewsets
from ..serializers.cliente_serializer import ClienteSerializer
from ...models import Cliente


class ClientesViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer