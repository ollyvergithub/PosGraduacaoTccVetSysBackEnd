from rest_framework import serializers
from ...models import Raca


class RacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raca
        fields = '__all__'


class RacaLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raca
        fields = ('uuid', 'nome', 'descricao')

