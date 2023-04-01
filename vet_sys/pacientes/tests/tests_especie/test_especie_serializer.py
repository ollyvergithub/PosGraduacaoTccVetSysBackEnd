import pytest
from vet_sys.pacientes.api.serializers.especie_serializer import EspecieSerializer

pytestmark = pytest.mark.django_db


def test_serializer(especie_canina):
    serializer = EspecieSerializer(especie_canina)
    assert serializer.data is not None
    assert serializer.data['criado_em']
    assert serializer.data['alterado_em']
    assert serializer.data['id']
    assert serializer.data['nome']
    assert serializer.data['descricao']
