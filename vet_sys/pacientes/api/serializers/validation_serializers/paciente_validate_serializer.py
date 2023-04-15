from rest_framework import serializers

from vet_sys.pacientes.models import Paciente


class GerarRelatorioPdfValidateSerializer(serializers.Serializer): # noqa
    uuids_pacientes = serializers.ListField(required=True)

    def validate_uuids_pacientes(self, value): # noqa
        if len(value) == 0:
            raise serializers.ValidationError(f"É necessário informar ao menos um uuid de paciente.")

        for uuid in value:
            try:
                Paciente.objects.get(uuid=uuid)
            except Paciente.DoesNotExist: # noqa
                raise serializers.ValidationError(f"Não foi encontrado um Paciente para o uuid {uuid}.")

        return value
