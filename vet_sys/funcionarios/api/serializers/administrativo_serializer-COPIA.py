from rest_framework import serializers

from ...models import Administrativo, Dependente
from vet_sys.funcionarios.api.serializers.dependente_serializer import DependenteCreateSerializer, DependenteSerializer


class AdministrativoCreateSerializer(serializers.ModelSerializer):
    dependentes = DependenteCreateSerializer(many=True, required=False)

    def create(self, validated_data):
        dependentes = validated_data.pop('dependentes')

        administrativo = Administrativo.objects.create(**validated_data)

        dependentes_lista = []
        for dependente in dependentes:
            dependente_object = DependenteCreateSerializer().create(dependente)
            dependentes_lista.append(dependente_object)

        administrativo.dependentes_do_funcionario.set(dependentes_lista)
        administrativo.save()

        return administrativo

    def update(self, instance, validated_data):
        dependentes = validated_data.pop('dependentes')

        # Atualiza campos do Funcionario
        Administrativo.objects.filter(uuid=instance.uuid).update(**validated_data)

        # Atualiza os dependentes
        keep_dependentes = []  # dependentes que serão mantidos. Qualquer um que não estiver na lista será apagado.

        for dependente in dependentes:
            if "uuid" in dependente.keys():
                if Dependente.objects.filter(uuid=dependente['uuid']).exists():
                    Dependente.objects.filter(uuid=dependente["uuid"]).update(**dependente)
                    dependente_updated = Dependente.objects.get(uuid=dependente["uuid"])
                    dependente_updated.save()
                    keep_dependentes.append(dependente_updated.uuid)
                else:
                    continue
            else:
                dependente_updated = Dependente.objects.create(**dependente, funcionario=instance)
                keep_dependentes.append(dependente_updated.uuid)

        # Apaga dependentes do funcionario que não estão na lista de dependentes a serem mantidos
        for dependente in instance.dependentes_do_funcionario.all():
            if dependente.uuid not in keep_dependentes:
                dependente.delete()

        # Retorna o funcionario atualizado
        funcionario_updated = Administrativo.objects.get(uuid=instance.uuid)
        funcionario_updated.save()

        return funcionario_updated

    class Meta:
        model = Administrativo
        exclude = ('id',)


class AdministrativoLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrativo
        fields = (
            'id', 'uuid', 'nome', 'cpf', 'rg', 'sexo', 'data_de_nascimento',
        )


class AdministrativoSerializer(serializers.ModelSerializer):
    dependentes_do_funcionario = DependenteSerializer(many=True)

    class Meta:
        model = Administrativo
        fields = (
            'id', 'uuid', 'nome', 'cpf', 'rg', 'sexo', 'tipo_logradouro', 'logradouro', 'numero', 'bairro',
            'complemento', 'cep', 'telefone', 'data_de_nascimento', 'email', 'descricao', 'criado_em',
            'dependentes_do_funcionario'
        )
