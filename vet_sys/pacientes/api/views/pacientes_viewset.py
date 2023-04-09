from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers.paciente_serializer import PacienteSerializer
from ...models import Paciente


class PacientesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'uuid'
    queryset = Paciente.objects.all().order_by('id',)
    serializer_class = PacienteSerializer

    def get_queryset(self):
        qs = Paciente.objects.all()
        nome = self.request.query_params.get('nome')
        if nome:
            qs = qs.filter(nome__unaccent__icontains=nome)

        cliente_uuid = self.request.query_params.get('cliente_uuid')
        if cliente_uuid:
            qs = qs.filter(tutor__uuid=cliente_uuid)

        especie_uuid = self.request.query_params.get('especie_uuid')
        if especie_uuid:
            qs = qs.filter(especie__uuid=especie_uuid)

        raca_uuid = self.request.query_params.get('raca_uuid')
        if raca_uuid:
            qs = qs.filter(raca__uuid=raca_uuid)

        return qs
