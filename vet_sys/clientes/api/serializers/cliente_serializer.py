from rest_framework import serializers
from ...models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    from vet_sys.pacientes.api.serializers.paciente_serializer import PacienteLookupSerializer
    paciente = PacienteLookupSerializer(many=True)

    class Meta:
        model = Cliente
        fields = (
        'uuid', 'nome', 'cpf', 'sexo', 'paciente', 'tipo_logradouro', 'logradouro', 'numero', 'bairro', 'complemento', 'cep', 'ddd',
        'telefone', 'ddd_segundo_telefone', 'segundo_telefone', 'data_de_nascimento', 'email')


class ClienteLookupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = (
        'uuid', 'nome', 'cpf', 'sexo', 'tipo_logradouro', 'logradouro', 'numero', 'bairro', 'complemento', 'cep', 'ddd',
        'telefone', 'ddd_segundo_telefone', 'segundo_telefone', 'data_de_nascimento', 'email')
