from rest_framework import serializers

from vet_sys.clientes.models import Cliente


class GerarRelatorioPdfValidateSerializer(serializers.Serializer): # noqa
    uuids_clientes = serializers.ListField(required=True)

    def validate_uuids_clientes(self, value): # noqa
        if len(value) == 0:
            raise serializers.ValidationError(f"É necessário informar ao menos um uuid de cliente.")

        for uuid in value:
            try:
                Cliente.objects.get(uuid=uuid)
            except Cliente.DoesNotExist: # noqa
                raise serializers.ValidationError(f"Não foi encontrado um Cliente para o uuid {uuid}.")

        return value