from rest_framework import viewsets
from ..serializers.paciente_serializer import PacienteSerializer
from ...models import Paciente


class PacientesViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
