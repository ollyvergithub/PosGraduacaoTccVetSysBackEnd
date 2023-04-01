import pytest
from vet_sys.clientes.api.serializers.cliente_serializer import ClienteSerializer

pytestmark = pytest.mark.django_db


def test_serializer(cliente_susi_clientes):
    serializer = ClienteSerializer(cliente_susi_clientes)
    assert serializer.data is not None
    assert serializer.data['uuid']
    assert serializer.data['nome']
    assert serializer.data['sexo']
    assert serializer.data['paciente']
    assert serializer.data['descricao']
