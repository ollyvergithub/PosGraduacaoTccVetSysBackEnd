from rest_framework import serializers
from ...models import Especie


class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'


class EspecieLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = ('uuid', 'nome', 'descricao')

