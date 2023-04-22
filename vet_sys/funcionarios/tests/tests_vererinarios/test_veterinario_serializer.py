import pytest
from vet_sys.funcionarios.api.serializers.administrativo_serializer import AdministrativoSerializer
from vet_sys.funcionarios.api.serializers.veterinario_serializer import VeterinarioSerializer

pytestmark = pytest.mark.django_db


def test_serializer(funcionario_veterinario_susi):
    serializer = VeterinarioSerializer(funcionario_veterinario_susi)
    assert serializer.data is not None
    assert serializer.data['uuid']
    assert serializer.data['nome']
    assert serializer.data['sexo']
    assert serializer.data['cpf']
    assert serializer.data['crmv']
    assert serializer.data['descricao']
