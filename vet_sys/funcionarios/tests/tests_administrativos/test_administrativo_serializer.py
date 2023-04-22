import pytest
from vet_sys.funcionarios.api.serializers.administrativo_serializer import AdministrativoSerializer

pytestmark = pytest.mark.django_db


def test_serializer(funcionario_administrativo_ollyver):
    serializer = AdministrativoSerializer(funcionario_administrativo_ollyver)
    assert serializer.data is not None
    assert serializer.data['uuid']
    assert serializer.data['nome']
    assert serializer.data['sexo']
    assert serializer.data['cpf']
    assert serializer.data['rg']
    assert serializer.data['descricao']
