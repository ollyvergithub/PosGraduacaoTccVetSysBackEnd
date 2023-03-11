from rest_framework import serializers
from ...models import Paciente
from .especie_serializer import EspecieLookupSerializer
from .raca_serializer import RacaLookupSerializer
from .porte_serializer import PorteLookupSerializer


class PacienteSerializer(serializers.ModelSerializer):

    especie = EspecieLookupSerializer(many=False)
    raca = RacaLookupSerializer(many=False)
    porte = PorteLookupSerializer(many=False)
    tutor = serializers.SerializerMethodField('get_tutor')

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
        fields = ('uuid', 'nome', 'especie', 'raca', 'porte', 'sexo', 'tutor', 'data_nasc', 'pelagem', 'cor')


class PacienteLookupSerializer(serializers.ModelSerializer):
    especie = EspecieLookupSerializer(many=False)
    raca = RacaLookupSerializer(many=False)
    porte = PorteLookupSerializer(many=False)

    class Meta:
        model = Paciente
        fields = ('uuid', 'nome', 'especie', 'raca', 'porte', 'sexo', 'data_nasc', 'pelagem', 'cor')


