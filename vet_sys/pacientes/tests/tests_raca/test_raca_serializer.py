import pytest
from vet_sys.pacientes.api.serializers.raca_serializer import RacaSerializer

pytestmark = pytest.mark.django_db


def test_serializer(raca_schnauzer):
    serializer = RacaSerializer(raca_schnauzer)
    assert serializer.data is not None
    assert serializer.data['criado_em']
    assert serializer.data['alterado_em']
    assert serializer.data['id']
    assert serializer.data['nome']
    assert serializer.data['descricao']
