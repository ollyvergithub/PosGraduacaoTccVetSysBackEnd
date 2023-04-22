from rest_framework import serializers
from vet_sys.funcionarios.models import Administrativo

class GerarRelatorioPdfValidateSerializer(serializers.Serializer): # noqa
    uuids_administrativos = serializers.ListField(required=True)

    def validate_uuids_administrativos(self, value): # noqa
        if len(value) == 0:
            raise serializers.ValidationError(f"É necessário informar ao menos um uuid de funcionário administrativo.")

        for uuid in value:
            try:
                Administrativo.objects.get(uuid=uuid)
            except Administrativo.DoesNotExist: # noqa
                raise serializers.ValidationError(f"Não foi encontrado um Funcionário Administrativo para o uuid {uuid}.")

        return value