from rest_framework import serializers
from ...models import Veterinario


class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = (
            'id', 'uuid', 'nome', 'cpf', 'crmv', 'sexo', 'tipo_logradouro', 'logradouro', 'numero', 'bairro',
            'complemento', 'cep', 'telefone', 'data_de_nascimento', 'email', 'descricao', 'criado_em'
        )
