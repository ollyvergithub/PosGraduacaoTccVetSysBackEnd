from rest_framework import serializers
from vet_sys.funcionarios.models import Veterinario

class GerarRelatorioPdfValidateSerializer(serializers.Serializer): # noqa
    uuids_veterinarios = serializers.ListField(required=True)

    def validate_uuids_veterinarios(self, value): # noqa
        if len(value) == 0:
            raise serializers.ValidationError(f"É necessário informar ao menos um uuid de veterinário.")

        for uuid in value:
            try:
                Veterinario.objects.get(uuid=uuid)
            except Veterinario.DoesNotExist: # noqa
                raise serializers.ValidationError(f"Não foi encontrado um Veterinário para o uuid {uuid}.")

        return value