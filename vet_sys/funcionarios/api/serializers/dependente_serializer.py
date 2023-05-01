from rest_framework import serializers

from ...models import Dependente, Administrativo


class DependenteCreateSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(required=False)

    class Meta:
        model = Dependente
        exclude = ('id', 'funcionario')


class DependenteSerializer(serializers.ModelSerializer):
    funcionario = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        allow_null=True,
        queryset=Administrativo.objects.all()
    )

    class Meta:
        model = Dependente
        fields = (
            'id', 'uuid', 'nome', 'sexo', 'data_de_nascimento', 'funcionario', 'criado_em'
        )
