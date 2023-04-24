from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ...models.consulta import Consulta
from ..serializer.consulta_serializer import ConsultaSerializer


class ConsultasViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'uuid'
    queryset = Consulta.objects.all().order_by('id', )
    serializer_class = ConsultaSerializer