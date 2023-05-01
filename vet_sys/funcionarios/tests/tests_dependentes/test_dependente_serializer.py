import pytest
from vet_sys.funcionarios.api.serializers.dependente_serializer import DependenteSerializer

pytestmark = pytest.mark.django_db


def test_serializer(dependente_01):
    serializer = DependenteSerializer(dependente_01)
    assert serializer.data is not None
    assert serializer.data['id']
    assert serializer.data['uuid']
    assert serializer.data['nome']
    assert serializer.data['sexo']
    assert serializer.data['data_de_nascimento']
    assert serializer.data['funcionario']
