from rest_framework import serializers

from vet_sys.pacientes.models import Paciente
from ...models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    from vet_sys.pacientes.api.serializers.paciente_serializer import PacienteLookupSerializer

    paciente = serializers.PrimaryKeyRelatedField(queryset=Paciente.objects.all(), many=True)

    paciente_detail = PacienteLookupSerializer(source='paciente', read_only=True, many=True)

    class Meta:
        model = Cliente
        fields = (
            'id', 'uuid', 'nome', 'cpf', 'sexo', 'paciente', 'paciente_detail', 'tipo_logradouro', 'logradouro',
            'numero', 'bairro', 'complemento', 'cep', 'ddd',
            'telefone', 'ddd_segundo_telefone', 'segundo_telefone', 'data_de_nascimento', 'email', 'descricao', 'criado_em'
        )


class ClienteLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id', 'uuid', 'nome', 'cpf', 'sexo', 'tipo_logradouro', 'logradouro', 'numero', 'bairro', 'complemento',
            'cep', 'ddd',
            'telefone', 'ddd_segundo_telefone', 'segundo_telefone', 'data_de_nascimento', 'email', 'descricao'
        )
