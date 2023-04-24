from rest_framework import serializers

from vet_sys.consultas.models import Consulta
from vet_sys.pacientes.models import Paciente
from vet_sys.clientes.models import Cliente
from vet_sys.funcionarios.models import Veterinario
from vet_sys.pacientes.api.serializers import PacienteLookupSerializer
from vet_sys.clientes.api.serializers import ClienteLookupSerializer
from vet_sys.funcionarios.api.serializers import VeterinarioSerializer


class ConsultaSerializer(serializers.ModelSerializer):
    paciente_detail = PacienteLookupSerializer(source='paciente', read_only=True)

    paciente = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        allow_null=True,
        queryset=Paciente.objects.all()
    )

    cliente_detail = ClienteLookupSerializer(source='cliente', read_only=True)
    cliente = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        allow_null=True,
        queryset=Cliente.objects.all()
    )

    veterinario_detail = VeterinarioSerializer(source='veterinario', read_only=True)
    veterinario = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        allow_null=True,
        queryset=Veterinario.objects.all()
    )

    class Meta:
        model = Consulta
        fields = (
            'id',
            'uuid',
            'data_da_consulta',
            'paciente',
            'paciente_detail',
            'cliente',
            'cliente_detail',
            'veterinario',
            'veterinario_detail',
            'tipo_de_consulta',
            'ficha_clinica',
        )
