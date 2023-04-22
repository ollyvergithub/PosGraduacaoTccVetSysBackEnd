from rest_framework import serializers
from ...models import Administrativo


class AdministrativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrativo
        fields = (
            'id', 'uuid', 'nome', 'cpf', 'rg', 'sexo', 'tipo_logradouro', 'logradouro', 'numero', 'bairro',
            'complemento', 'cep', 'telefone', 'data_de_nascimento', 'email', 'descricao', 'criado_em'
        )
