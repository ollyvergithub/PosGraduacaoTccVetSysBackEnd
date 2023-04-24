from rest_framework import serializers

from vet_sys.clientes.models import Cliente
from vet_sys.consultas.models import Consulta


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