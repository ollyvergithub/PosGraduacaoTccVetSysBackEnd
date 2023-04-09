from rest_framework import serializers

from vet_sys.clientes.models import Cliente
from ...models import Paciente, Especie, Raca, Porte
from .especie_serializer import EspecieLookupSerializer
from .raca_serializer import RacaLookupSerializer
from .porte_serializer import PorteLookupSerializer


class PacienteSerializer(serializers.ModelSerializer):
    especie_detail = EspecieLookupSerializer(source='especie', read_only=True)
    especie = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        allow_null=True,
        queryset=Especie.objects.all()
    )

    raca_detail = RacaLookupSerializer(source='raca', read_only=True)
    raca = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        allow_null=True,
        queryset=Raca.objects.all()
    )

    porte_detail = PorteLookupSerializer(source='porte', read_only=True)
    porte = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        allow_null=True,
        queryset=Porte.objects.all()
    )

    tutor_detail = serializers.SerializerMethodField('get_tutor')

    tutor = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        allow_null=True,
        queryset=Cliente.objects.all()
    )

    def get_tutor(self, obj):
        obj_cliente = {
            "uuid": None,
            "nome": None,
            "cpf": None,
        }

        tutor = obj.tutor

        if tutor:
            obj_cliente = {
                "uuid": tutor.uuid,
                "nome": tutor.nome,
                "cpf": tutor.cpf,
            }
        return obj_cliente

    class Meta:
        model = Paciente
        fields = (
            'id', 'uuid', 'nome', 'especie', 'especie_detail', 'raca', 'raca_detail', 'porte', 'porte_detail', 'sexo',
            'peso', 'tutor', 'tutor_detail', 'data_nasc', 'pelagem', 'cor', 'descricao'
        )


class PacienteLookupSerializer(serializers.ModelSerializer):
    especie = EspecieLookupSerializer(many=False)
    raca = RacaLookupSerializer(many=False)
    porte = PorteLookupSerializer(many=False)

    class Meta:
        model = Paciente
        fields = (
            'id', 'uuid', 'nome', 'especie', 'raca', 'porte', 'sexo', 'peso', 'data_nasc', 'pelagem', 'cor',
            'descricao')
