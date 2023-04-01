import pytest
from vet_sys.pacientes.api.serializers.porte_serializer import PorteSerializer

pytestmark = pytest.mark.django_db


def test_serializer(porte_mini):
    serializer = PorteSerializer(porte_mini)
    assert serializer.data is not None
    assert serializer.data['criado_em']
    assert serializer.data['alterado_em']
    assert serializer.data['id']
    assert serializer.data['porte']
    assert serializer.data['descricao']
