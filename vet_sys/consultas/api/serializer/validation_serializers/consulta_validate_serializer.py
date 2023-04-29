from rest_framework import serializers

from vet_sys.consultas.models import Consulta
from vet_sys.pacientes.models import Paciente


class GerarRelatorioPdfValidateSerializer(serializers.Serializer): # noqa
    uuids_consultas = serializers.ListField(required=True)

    def validate_uuids_consultas(self, value): # noqa
        if len(value) == 0:
            raise serializers.ValidationError(f"É necessário informar ao menos um uuid de consulta.")

        for uuid in value:
            try:
                Consulta.objects.get(uuid=uuid)
            except Consulta.DoesNotExist: # noqa
                raise serializers.ValidationError(f"Não foi encontrado uma Consulta para o uuid {uuid}.")

        return value


class ConsultaPacienteValidateSerializer(serializers.Serializer): # noqa
    paciente = serializers.CharField(required=True)
    consulta = serializers.CharField(required=False)

    def validate_paciente(self, value): # noqa
        try:
            Paciente.objects.get(uuid=value)
        except Paciente.DoesNotExist:  # noqa
            erro = {
                'erro': 'Objeto não encontrado.',
                'mensagem': f"O objeto Paciente para o uuid {value} não foi encontrado na base."
            }
            raise serializers.ValidationError(erro)

        return value

    def validate_consulta(self, value):  # noqa
        if value:
            try:
                Consulta.objects.get(uuid=value)
            except Consulta.DoesNotExist:  # noqa
                erro = {
                    'erro': 'Objeto não encontrado.',
                    'mensagem': f"O objeto Consulta para o uuid {value} não foi encontrado na base."
                }
                raise serializers.ValidationError(erro)

            return value
