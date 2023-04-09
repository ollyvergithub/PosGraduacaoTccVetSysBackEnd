from rest_framework import serializers
from ...models import Porte


class PorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Porte
        fields = '__all__'


class PorteLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Porte
        fields = ('uuid', 'porte', 'descricao', 'get_porte_display')

